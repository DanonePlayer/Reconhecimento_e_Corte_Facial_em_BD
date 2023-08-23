import os
from os.path import join as pjoin

import cv2
import numpy as np
from PIL import Image


def recortes(genero):
    #Abre a pasta IMAGENS + o genero especificado e lista ela
    imagens = os.listdir(f"IMAGENS-{genero}")

    for imgi in imagens:
        #Abre o arquivo = pasta + o arquivo + o genero especificado
        img = Image.open(f"IMAGENS-{genero}/{imgi}")
        # tranforma o tamanho da imagem, (redimensiona)
        if img.width != 321 or img.height != 380:
            print(img + "Precisa Redimensionar")

            # Redimensiona
            img_resized = img.resize((321, 380))
            #salva
            img_resized.save(f"IMAGENS-{genero}/{imgi}")
            # outra forma height = img.height + 400

        #corta a imagem para os olhos
        #abre a imagem
        Image1 = Image.open(f"IMAGENS-{genero}\{imgi}") 
        croppedIm = Image1.crop((84, 123, 261, 195)) 
        # croppedIm.show()
        path_to_file = pjoin(f"Olhos-{genero}",imgi)
        croppedIm.save(path_to_file)


        #corta a imagem para o nariz
        # Carrega a imagem
        img = cv2.imread(f"IMAGENS-{genero}\{imgi}")

        # Define os pontos dos vértices
        pts = np.array([[112, 184], [140, 184], [140, 133], [177, 133], [177, 184], [205, 184], [205, 238], [112, 238]], np.int32)

        # Cria uma máscara com os pontos
        mask = np.zeros_like(img)
        cv2.fillPoly(mask, [pts], (255, 255, 255))

        # Aplica a máscara na imagem original
        img_cortada = cv2.bitwise_and(img, mask)

        # Exibe a imagem triangular
        # cv2.imshow(f'{imgi}', img_cortada)
        cv2.imwrite(f"Nariz-{genero}\{imgi}", img_cortada) 



        #aqui iremos transforma o redor da imagem em transparente
        #abre a imagem
        img = Image.open(f"Nariz-{genero}\{imgi}")
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



        #corta a imagem para a boca
        Image1 = Image.open(f"IMAGENS-{genero}\{imgi}")
        croppedIm = Image1.crop((112, 234, 220, 278))
        # croppedIm.show()
        path_to_file = pjoin(f"Boca-{genero}",imgi)
        croppedIm.save(path_to_file)



        #Corta a imagem em todos as partes para o rosto
        # Carrega a imagem
        img = cv2.imread(f"IMAGENS-{genero}\{imgi}")

        # Define os pontos dos vértices
        pts = np.array( [[85, 194],[85, 124],[260, 124],[260, 194], [203, 194], [203, 235], [217, 235], [217, 278], [112, 278], [112, 194]], np.int32)

        # Cria uma máscara com os pontos
        mask = np.zeros_like(img)
        cv2.fillPoly(mask, [pts], (255, 255, 255))

        # Aplica a máscara na imagem original
        img_cortada = cv2.bitwise_and(img, mask)
        part_cortada = cv2.bitwise_and(img, cv2.bitwise_not(mask))
        # cv2.imshow('Parte Cortada', part_cortada)
        # part_cortada = cv2.resize(part_cortada, (341, 400))
        cv2.imwrite(f"Rosto-{genero}\{imgi}", part_cortada) 

        img = Image.open(f"Rosto-{genero}\{imgi}")
        rgba = img.convert("RGBA")
        datas = rgba.getdata()
        
        newData = []
        for item in datas:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)
        rgba.putdata(newData)
        rgba.save(f"Rosto-{genero}\{imgi}", "PNG")
        print(imgi)



        # imagens = os.listdir(f"Tronco-{genero}")
        # img = imagens[n_imagen]
        # print(imagens[n_imagen])
        # img = Image.open(f"Tronco-{genero}/{imgi}")
        # img_resized = img.resize((321, 380))
        # img_resized.save(f"Tronco-{genero}/{imgi}")

        # imagens = os.listdir(f"Olhos-{genero}")
        # img = imagens[n_imagen]
        # img = Image.open(f"Olhos-{genero}/{imgi}")
        # img_resized = img.resize((176, 67))
        # img_resized.save(f"Olhos-{genero}/{imgi}")

        # imagens = os.listdir(f"Nariz-{genero}")
        # img = imagens[n_imagen]
        # img = Image.open(f"Nariz-{genero}/{imgi}")
        # img_resized = img.resize((321, 380))
        # img_resized.save(f"Nariz-{genero}/{imgi}")

        # imagens = os.listdir(f"Boca-{genero}")
        # img = imagens[n_imagen]
        # img = Image.open(f"Boca-{genero}/{imgi}")
        # img_resized = img.resize((106, 42))
        # img_resized.save(f"Boca-{genero}/{imgi}")

        # n_imagen +=1




