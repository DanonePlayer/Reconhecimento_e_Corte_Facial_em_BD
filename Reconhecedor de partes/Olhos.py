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
    objetos = classificador.detectMultiScale(imgGray, minSize=(120,120), scaleFactor=1.1, minNeighbors=10, maxSize=(950,220))

    for x,y,l,a in objetos:
        pass

    try:
        olho_esquerdo = objetos[0]
        olho_direito = objetos[1]
        cont = 1
    except:
        print("vixx")
        cont = 0
        img_corte = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # tranforma o tamanho da imagem, (redimensiona)
        if img_corte.width != 659 and img_corte.height != 711:
            print(f"{img_corte} + Precisa Redimensionar")

            # Redimensiona
            img_corte = img_corte.resize((659, 711))
            #salva
            # img_corte.save(f"IMAGENS-{genero}/{imgi}")

        croppedIm = img_corte.crop((159, 246, 524, 384)) 
        # croppedIm.show()
        path_to_file = pjoin(f"Olhos-{genero}",imgi)
        croppedIm.save(path_to_file)



    if cont == 1:
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        pontos = [[olho_direito[0], olho_direito[1]],  
                        [olho_direito[0], olho_direito[1]+olho_direito[3]], 
                        [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]+olho_esquerdo[3]], 
                        [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]]]
        try:
            croppedIm = img.crop((olho_direito[0], olho_direito[1], olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]+olho_esquerdo[3]))
            path_to_file = pjoin(f"Olhos-{genero}",imgi)
            croppedIm.save(path_to_file)
            print(pontos)
            # print(pontos[0][0])
        except:
            if pontos[0][0] > pontos[0][1]:
                olho_esquerdo = objetos[1]
                olho_direito = objetos[0]
                pontos = [[olho_direito[0], olho_direito[1]],  
                    [olho_direito[0], olho_direito[1]+olho_direito[3]], 
                    [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]+olho_esquerdo[3]], 
                    [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]]]
                croppedIm = img.crop((olho_direito[0], olho_direito[1], olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]+olho_esquerdo[3])) 
                path_to_file = pjoin(f"Olhos-{genero}",imgi)
                croppedIm.save(path_to_file)
            print(pontos)


    # plt.imshow(img)
    # plt.imshow(img_cortada)
    # plt.imshow(part_cortada)
    # plt.axis('off')
    # plt.show()

    # Melhores hass

    # olhos = right_eye2