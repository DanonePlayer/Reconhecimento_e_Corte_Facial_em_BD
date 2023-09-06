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
        if img.width > 659 or img.height > 711:
            print(f"{img} + Precisa Redimensionar")
            widht = img.width - 100
            height = img.height - 10
            # Redimensiona
            img_resized = img.resize((widht, height))
            #salva
            img_resized.save(f"IMAGENS-{genero}/{imgi}")
        elif img.width < 659 or img.height < 711:
            print(f"{img} + Precisa Redimensionar")
            widht = img.width + 50
            height = img.height + 50
            # Redimensiona
            img_resized = img.resize((widht, height))
            #salva
            img_resized.save(f"IMAGENS-{genero}/{imgi}")
            
recortes("M")


# pts = np.array([[232, 242], [232, 360], [610, 350], [610, 231]], np.int32)