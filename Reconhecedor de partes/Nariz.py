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

    classificador = cv2.CascadeClassifier(r"anexos/nose.xml")
    img = cv2.imread(f"IMAGENS-{genero}/{imgi}")


    imgGray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    # cv2.imshow('Imagem Cinza', imgGray)
    objetos = classificador.detectMultiScale(imgGray, minSize=(120,120), scaleFactor=1.6, maxSize=(950,220))
    #print(objetos)

    for x,y,l,a in objetos:
        pass
        # print(objetos)
        cv2.rectangle(img,(x,y-120),(x+l+15,y+a),(255, 0, 0), 2)

    try:
        Nariz = objetos[0]
        cont = 1
    except:
        print("vixx")
        cont = 0
        img_corte = Image.open(f"IMAGENS-{genero}/{imgi}")
        # tranforma o tamanho da imagem, (redimensiona)
        if img_corte.width > 659 or img_corte.height > 711:
            print(f"{img_corte} + Precisa Redimensionar")
            widht = img_corte.width - 100
            height = img_corte.height - 10
            # Redimensiona
            img_resized = img_corte.resize((widht, height))
            #salva
            img_resized.save(f"IMAGENS-{genero}/{imgi}")
        elif img_corte.width < 659 or img_corte.height < 711:
            print(f"{img_corte} + Precisa Redimensionar")
            widht = img_corte.width + 50
            height = img_corte.height + 50
            # Redimensiona
            img_resized = img_corte.resize((widht, height))
            #salva
            img_resized.save(f"IMAGENS-{genero}/{imgi}")

    if cont == 1:
    
        # img = cv2.imread("hascas/rosto.png")
        pts = np.array( [[Nariz[0], Nariz[1]-120],  
                        [Nariz[0], Nariz[1]+Nariz[3]], 
                        [Nariz[0]+Nariz[2], Nariz[1]+Nariz[3]], 
                        [Nariz[0]+Nariz[2], Nariz[1]-120]], np.int32)

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





    plt.imshow(img)
    # plt.imshow(img_cortada)
    # plt.imshow(part_cortada)
    plt.axis('off')
    plt.show()