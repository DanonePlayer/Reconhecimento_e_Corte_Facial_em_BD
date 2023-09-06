import os
from os.path import join as pjoin

import cv2
import numpy as np
from PIL import Image

#corta a imagem para o nariz
# Carrega a imagem
img = cv2.imread("IMAGENS-M\TESTE-1.png")

# Define os pontos dos vértices
pts = np.array([[159, 246], [159, 387], [524, 384], [524, 246]], np.int32)

# Cria uma máscara com os pontos
mask = np.zeros_like(img)
cv2.fillPoly(mask, [pts], (255, 255, 255))

# Aplica a máscara na imagem original
img_cortada = cv2.bitwise_and(img, mask)

# Exibe a imagem triangular

cv2.imshow('Imagem cortada', img_cortada) #img #img_cortada #part_cortada
cv2.waitKey(0)
cv2.destroyAllWindows()