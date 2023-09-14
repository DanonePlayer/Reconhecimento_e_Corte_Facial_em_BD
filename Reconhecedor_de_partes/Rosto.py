#USA O rosto.png COMO EXEMPLO DE TESTE, ELE É MAIS COMO UMA BASE, É PARECIDO COM MUITAS DAS IMAGENS DA BASE QUE VAMOS USAR
import os

import cv2
import numpy as np
from PIL import Image


def reconhecimento_e_corte_Rosto():
    genero = "M"
    imagens = os.listdir(f"IMAGENS-{genero}")
    for imgi in imagens:
        print(imgi)
        classificador = cv2.CascadeClassifier(r"anexos/right_eye2.xml")
        img = cv2.imread(f"IMAGENS-{genero}/{imgi}")
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        objetos = classificador.detectMultiScale(imgGray, minSize=(120,120), scaleFactor=1.1, minNeighbors=10, maxSize=(950,220))
        try:
            olho_esquerdo = objetos[0]
            olho_direito = objetos[1]
            cont = 1
        except:
            print("vixx, olho")
            cont = 0
            img_corte = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            # tranforma o tamanho da imagem, (redimensiona)
            if img_corte.width != 659 and img_corte.height != 711:
                print(f"{img_corte} + Precisa Redimensionar")

                # Redimensiona
                img_resized = img_corte.resize((659, 711))
                #salva
                img_resized.save(f"IMAGENS-{genero}/{imgi}")
            img_corte = cv2.cvtColor(np.array(img_corte), cv2.COLOR_RGB2BGR)
            # Define os pontos dos vértices
            pts = np.array([[159, 246], [159, 387], [524, 384], [524, 246]], np.int32)

            # Cria uma máscara com os pontos
            mask = np.zeros_like(img_corte)
            cv2.fillPoly(mask, [pts], (255, 255, 255))

            # Aplica a máscara na imagem original
            img_cortada = cv2.bitwise_and(img_corte, mask)
            part_cortada = cv2.bitwise_and(img_corte, cv2.bitwise_not(mask))

        if cont == 1:
            pts = np.array( [[olho_direito[0], olho_direito[1]],  
                            [olho_direito[0], olho_direito[1]+olho_direito[3]], 
                            [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]+olho_esquerdo[3]], 
                            [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]]], np.int32)

            pontos = [[olho_direito[0], olho_direito[1]],  
                            [olho_direito[0], olho_direito[1]+olho_direito[3]], 
                            [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]+olho_esquerdo[3]], 
                            [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]]]
            # print(pontos)

            if pontos[0][0] > pontos[0][1]:
                olho_esquerdo = objetos[1]
                olho_direito = objetos[0]
                pts = np.array( [[olho_direito[0], olho_direito[1]],  
                    [olho_direito[0], olho_direito[1]+olho_direito[3]], 
                    [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]+olho_esquerdo[3]], 
                    [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]]], np.int32)

                pontos = [[olho_direito[0], olho_direito[1]],  
                    [olho_direito[0], olho_direito[1]+olho_direito[3]], 
                    [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]+olho_esquerdo[3]], 
                    [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]]]
                
                # print(pontos)
            # Cria uma máscara com os pontos
            mask = np.zeros_like(img)
            cv2.fillPoly(mask, [pts], (255, 255, 255))


            # Aplica a máscara na imagem original
            img_cortada = cv2.bitwise_and(img, mask)
            part_cortada = cv2.bitwise_and(img, cv2.bitwise_not(mask))



        classificador = cv2.CascadeClassifier(r"anexos/nose.xml")
        img = part_cortada
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        objetos = classificador.detectMultiScale(imgGray, minSize=(120,120), scaleFactor=1.6, maxSize=(950,220))
        try:
            Nariz = objetos[0]
            cont = 1
        except:
            print("vixx, nariz")
            cont = 0
            img_corte = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            # tranforma o tamanho da imagem, (redimensiona)
            if img_corte.width != 659 and img_corte.height != 711:
                print(f"{img_corte} + Precisa Redimensionar")

                # Redimensiona
                img_resized = img_corte.resize((659, 711))
                #salva
                img_resized.save(f"IMAGENS-{genero}/{imgi}")
            img_corte = cv2.cvtColor(np.array(img_corte), cv2.COLOR_RGB2BGR)
            # Define os pontos dos vértices
            pts = np.array([[226, 221], [226, 498], [415, 498], [415, 221]], np.int32)

            # Cria uma máscara com os pontos
            mask = np.zeros_like(img_corte)
            cv2.fillPoly(mask, [pts], (255, 255, 255))

            # Aplica a máscara na imagem original
            img_cortada = cv2.bitwise_and(img_corte, mask)
            part_cortada = cv2.bitwise_and(img_corte, cv2.bitwise_not(mask))

        if cont == 1:
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





        classificador = cv2.CascadeClassifier(r"anexos/mouth.xml")
        img = part_cortada
        objetos = classificador.detectMultiScale(imgGray, minSize=(90,90), scaleFactor=1.1, minNeighbors=190, maxSize=(950,220)) # ou maxSize
        try:
            boca = objetos[0]
            cont = 1
        except:
            print("vixx, boca")
            cont = 0
            img_corte = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            # tranforma o tamanho da imagem, (redimensiona)
            if img_corte.width != 659 and img_corte.height != 711:
                print(f"{img_corte} + Precisa Redimensionar")

                # Redimensiona
                img_resized = img_corte.resize((659, 711))
                #salva
                img_resized.save(f"IMAGENS-{genero}/{imgi}")
            img_corte = cv2.cvtColor(np.array(img_corte), cv2.COLOR_RGB2BGR)
            # Define os pontos dos vértices
            pts = np.array([[185, 486], [185, 614], [479, 614], [479, 486]], np.int32)
            # Cria uma máscara com os pontos
            mask = np.zeros_like(img_corte)
            cv2.fillPoly(mask, [pts], (255, 255, 255))

            # Aplica a máscara na imagem original
            img_cortada = cv2.bitwise_and(img_corte, mask)
            part_cortada = cv2.bitwise_and(img_corte, cv2.bitwise_not(mask))


        if cont == 1:

            # img = cv2.imread("hascas/rosto.png")
            pts = np.array( [[boca[0]-40, boca[1]],  
                            [boca[0]-40, boca[1]+boca[3]], 
                            [(boca[0]+40)+boca[2], boca[1]+boca[3]],
                            [(boca[0]+40)+boca[2], boca[1]]], np.int32)
            
            pontos = [[boca[0]-40, boca[1]],  
                            [boca[0]-40, boca[1]+boca[3]], 
                            [(boca[0]+40)+boca[2], boca[1]+boca[3]],
                            [(boca[0]+40)+boca[2], boca[1]]]
            
            # print(pontos)

            # Cria uma máscara com os pontos
            mask = np.zeros_like(img)
            cv2.fillPoly(mask, [pts], (255, 255, 255))


            # # Aplica a máscara na imagem original
            img_cortada = cv2.bitwise_and(img, mask)
            part_cortada = cv2.bitwise_and(img, cv2.bitwise_not(mask))



        # Converta a imagem para o formato RGB para exibição com matplotlib
        img_cortada = cv2.cvtColor(img_cortada, cv2.COLOR_BGR2RGB)
        part_cortada = cv2.cvtColor(part_cortada, cv2.COLOR_BGR2RGB)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


        #aqui iremos transforma o redor da imagem em transparente
        # Crie uma imagem Pillow (PIL) a partir da imagem RGB
        img = Image.fromarray(part_cortada)
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
        rgba.save(f"Rosto-{genero}\{imgi}", "PNG")


        # plt.imshow(img)
        # plt.imshow(img_cortada)
        # plt.imshow(part_cortada)
        # plt.axis('off')
        # plt.show()



        # Melhores hass

        # olhos = right_eye2