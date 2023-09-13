import os
from os.path import join as pjoin

import cv2
import numpy as np
from PIL import Image


def recortes():
    img = Image.open("IMAGENS-M/Teste-10.png")

    # Redimensiona
    img_corte = img.resize((350, 400))
    #salva
    img_corte.save("IMAGENS-M/Teste-10.png")

recortes()
# pts = np.array([[232, 242], [232, 360], [610, 350], [610, 231]], np.int32)