#USA O rosto.png COMO EXEMPLO DE TESTE, ELE É MAIS COMO UMA BASE, É PARECIDO COM MUITAS DAS IMAGENS DA BASE QUE VAMOS USAR
import os

import cv2
import numpy as np
from PIL import Image

from Reconhecedor_de_partes import Olhos


def reconhecimento_e_corte_Nariz(progressbar, valor):
    genero = "M"
    imagens = os.listdir(f"IMAGENS-{genero}")
    barra_carregamento_max = len(imagens) * 4
    
    cont_barra_de_carregamento = 0
    for imgi in imagens:
        print(imgi)
        cont_barra_de_carregamento +=1
        valor_mapeado = ((cont_barra_de_carregamento - 0) / (barra_carregamento_max - 0)) * (101 - 0)  # Mapeia para 0 a 100
        valor_mapeado += valor
        print(valor_mapeado)
        progressbar["value"] = valor_mapeado
        progressbar.update() 

        classificador = cv2.CascadeClassifier(r"anexos/nose.xml")
        img = cv2.imread(f"IMAGENS-{genero}/{imgi}")


        imgGray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        # cv2.imshow('Imagem Cinza', imgGray)
        objetos = classificador.detectMultiScale(imgGray, minSize=(120,120), scaleFactor=1.6, maxSize=(950,220))
        #print(objetos)

        for x,y,l,a in objetos:
            pass
            # print(objetos)
            # cv2.rectangle(img,(x,y-120),(x+l,y+a),(255, 0, 0), 2)

        try:
            Nariz = objetos[0]
            cont = 1
        except:
            print("vixx")
            cont = 0
            img_corte = Image.open(f"IMAGENS-{genero}/{imgi}")
            # tranforma o tamanho da imagem, (redimensiona)
            if img_corte.width != 659 and img_corte.height != 711:
                print(f"{img_corte} + Precisa Redimensionar")

                # Redimensiona
                img_resized = img_corte.resize((659, 711))
                #salva
                img_resized.save(f"IMAGENS-{genero}/{imgi}")

            # img = cv2.imread(f"IMAGENS-{genero}/{imgi}")

            # Define os pontos dos vértices
            pts = np.array([[226, 221], [226, 498], [415, 498], [415, 221]], np.int32)

            # Cria uma máscara com os pontos
            mask = np.zeros_like(img)
            cv2.fillPoly(mask, [pts], (255, 255, 255))

            # Aplica a máscara na imagem original
            img_cortada = cv2.bitwise_and(img, mask)
            part_cortada = cv2.bitwise_and(img, cv2.bitwise_not(mask))

        if cont == 1:
        
            # img = cv2.imread("hascas/rosto.png")
            pts = np.array( [[Nariz[0], Nariz[1]-120],  
                            [Nariz[0], Nariz[1]+Nariz[3]], 
                            [Nariz[0]+Nariz[2], Nariz[1]+Nariz[3]], 
                            [Nariz[0]+Nariz[2], Nariz[1]-120]], np.int32)
            
            pontos = [[Nariz[0], Nariz[1]-120],  
                            [Nariz[0], Nariz[1]+Nariz[3]], 
                            [Nariz[0]+Nariz[2], Nariz[1]+Nariz[3]], 
                            [Nariz[0]+Nariz[2], Nariz[1]-120]]
            # print(pontos)

            # Cria uma máscara com os pontos
            mask = np.zeros_like(img)
            cv2.fillPoly(mask, [pts], (255, 255, 255))


            # Aplica a máscara na imagem original
            img_cortada = cv2.bitwise_and(img, mask)
            part_cortada = cv2.bitwise_and(img, cv2.bitwise_not(mask))


        # Converta a imagem para o formato RGB para exibição com matplotlib
        img_cortada = cv2.cvtColor(img_cortada, cv2.COLOR_BGR2RGB)
        part_cortada = cv2.cvtColor(part_cortada, cv2.COLOR_BGR2RGB)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



        #aqui iremos transforma o redor da imagem em transparente
        # Crie uma imagem Pillow (PIL) a partir da imagem RGB
        img = Image.fromarray(img_cortada)
        #convertida para o modo RGBA que significa que ela terá canais vermelho, verde, azul e alfa (transparência).
        rgba = img.convert("RGBA")
        # Isso obtém os dados de pixel da imagem, que incluirão informações sobre a cor e transparência de cada pixel.
        datas = rgba.getdata()
        
        newData = []
        for item in datas:
            # encontrando a cor preta pelo seu valor RGB
            if item[0] == 0 and item[1] == 0 and item[2] == 0:  
                # Se o pixel for preto, ele é substituído por um pixel totalmente transparente
                #  (branco com alfa 0), indicando que ele será tornando transparente.
                newData.append((255, 255, 255, 0))
            else:
                # outras cores permanecem inalteradas
                newData.append(item)  
        # Aqui, os novos dados de pixel são aplicados à imagem RGBA.
        rgba.putdata(newData)
        #A imagem editada é salva
        rgba.save(f"Nariz-{genero}\{imgi}", "PNG")


        # plt.imshow(img)
        # plt.imshow(img_cortada)
        # plt.imshow(part_cortada)
        # plt.axis('off')
        # plt.show()
    
    Olhos.reconhecimento_e_corte_Olhos(progressbar, valor_mapeado)