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
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    objetos = classificador.detectMultiScale(imgGray, minSize=(120,120), scaleFactor=1.1, minNeighbors=10, maxSize=(950,220))

    for x,y,l,a in objetos:
        pass

    try:
        olho_esquerdo = objetos[0]
        olho_direito = objetos[1]
        cont = 1
    except:
        print("vixx, olho")
        cont = 0
        img_corte = Image.open(f"IMAGENS-{genero}/{imgi}")
        # tranforma o tamanho da imagem, (redimensiona)
        if img_corte.width != 659 and img_corte.height != 711:
            print(f"{img_corte} + Precisa Redimensionar")

            # Redimensiona
            img_resized = img_corte.resize((659, 711))
            #salva
            img_resized.save(f"IMAGENS-{genero}/{imgi}")

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
    for x,y,l,a in objetos:
        pass
    try:
        Nariz = objetos[0]
        cont = 1
    except:
        print("vixx, nariz")
        cont = 0
        img_corte = Image.open(f"IMAGENS-{genero}/{imgi}")
        # tranforma o tamanho da imagem, (redimensiona)
        if img_corte.width != 659 and img_corte.height != 711:
            print(f"{img_corte} + Precisa Redimensionar")

            # Redimensiona
            img_resized = img_corte.resize((659, 711))
            #salva
            img_resized.save(f"IMAGENS-{genero}/{imgi}")

        # Define os pontos dos vértices
        pts = np.array([[226, 221], [226, 498], [415, 498], [415, 221]], np.int32)

        # Cria uma máscara com os pontos
        mask = np.zeros_like(img)
        cv2.fillPoly(mask, [pts], (255, 255, 255))

        # Aplica a máscara na imagem original
        img_cortada = cv2.bitwise_and(img, mask)
        part_cortada = cv2.bitwise_and(img, cv2.bitwise_not(mask))

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

    for x,y,l,a in objetos:
        pass
        
    try:
        boca = objetos[0]
        cont = 1
    except:
        print("vixx, boca")
        cont = 0
        img_corte = Image.open(f"IMAGENS-{genero}/{imgi}")
        # tranforma o tamanho da imagem, (redimensiona)
        if img_corte.width != 659 and img_corte.height != 711:
            print(f"{img_corte} + Precisa Redimensionar")

            # Redimensiona
            img_resized = img_corte.resize((659, 711))
            #salva
            img_resized.save(f"IMAGENS-{genero}/{imgi}")

        # Define os pontos dos vértices
        pts = np.array([[185, 486], [185, 614], [479, 614], [479, 486]], np.int32)
        # Cria uma máscara com os pontos
        mask = np.zeros_like(img)
        cv2.fillPoly(mask, [pts], (255, 255, 255))

        # Aplica a máscara na imagem original
        img_cortada = cv2.bitwise_and(img, mask)
        part_cortada = cv2.bitwise_and(img, cv2.bitwise_not(mask))


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





    # plt.imshow(img)
    # plt.imshow(img_cortada)
    plt.imshow(part_cortada)
    plt.axis('off')
    plt.show()



    # Melhores hass

    # olhos = right_eye2