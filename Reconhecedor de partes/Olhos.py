#USA O rosto.png COMO EXEMPLO DE TESTE, ELE É MAIS COMO UMA BASE, É PARECIDO COM MUITAS DAS IMAGENS DA BASE QUE VAMOS USAR
import os
from os.path import join as pjoin

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

genero = "M"
imagens = os.listdir(f"IMAGENS-{genero}")
for imgi in imagens:
    print(imgi)
    classificador = cv2.CascadeClassifier(r"anexos/right_eye2.xml")
    img = cv2.imread(f"IMAGENS-{genero}/{imgi}")

    # print(imgi)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    # cv2.imshow('Imagem Cinza', imgGray)
    objetos = classificador.detectMultiScale(imgGray, minSize=(120,120), scaleFactor=1.1, minNeighbors=10, maxSize=(950,220))
    # print(objetos)

    for x,y,l,a in objetos:
        pass
        # cv2.rectangle(img,(x,y),(x+l,y+a),(255, 0, 0), 2)

    try:
        olho_esquerdo = objetos[0]
        olho_direito = objetos[1]
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
        pts = np.array([[159, 246], [159, 387], [524, 384], [524, 246]], np.int32)

        # Cria uma máscara com os pontos
        mask = np.zeros_like(img)
        cv2.fillPoly(mask, [pts], (255, 255, 255))

        # Aplica a máscara na imagem original
        img_cortada = cv2.bitwise_and(img, mask)
        part_cortada = cv2.bitwise_and(img, cv2.bitwise_not(mask))

    if cont == 1:
        pts = np.array( [[olho_direito[0], olho_direito[1]],  
                        [olho_direito[0], olho_direito[1]+olho_direito[3]], 
                        [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]+olho_esquerdo[3]], 
                        [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]]], np.int32)

        pontos = [[olho_direito[0], olho_direito[1]],  
                        [olho_direito[0], olho_direito[1]+olho_direito[3]], 
                        [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]+olho_esquerdo[3]], 
                        [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]]]
        print(pontos)
        # print(pontos[0][0])

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

        # Converta a imagem para o formato RGB para exibição com matplotlib
    img_cortada = cv2.cvtColor(img_cortada, cv2.COLOR_BGR2RGB)
    part_cortada = cv2.cvtColor(part_cortada, cv2.COLOR_BGR2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    # plt.imshow(img)
    # plt.imshow(img_cortada)
    # plt.imshow(part_cortada)
    # plt.axis('off')
    # plt.show()


# Image1 = Image.open(f"IMAGENS-{genero}\{imgi}") 
# croppedIm = Image1.crop((84, 123, 261, 195)) 
# # croppedIm.show()
# path_to_file = pjoin(f"Olhos-{genero}",imgi)
# croppedIm.save(path_to_file)


# [[256, 404], [256, 566], [766, 561], [766, 404]]
# croppedIm = Image1.crop((404, 256, 766, 561)) 



    # Melhores hass

    # olhos = right_eye2