#USA O javier-bardem3.jpg.png COMO EXEMPLO DE TESTE, ELE É MAIS COMO UMA BASE, É PARECIDO COM MUITAS DAS IMAGENS DA BASE QUE VAMOS USAR
import os
from os.path import join as pjoin

import cv2
import numpy as np
from PIL import Image

classificador = cv2.CascadeClassifier(r"anexos/eye.xml")
img = cv2.imread("hascas/rosto.png")


imgGray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
# cv2.imshow('Imagem Cinza', imgGray)
objetos = classificador.detectMultiScale(imgGray, minSize=(50,50), scaleFactor=1.5) # ou maxSize
#print(objetos)

for x,y,l,a in objetos:
    # print(objetos)
    cv2.rectangle(img,(x,y),(x+l,y+a),(255, 0, 0), 2)

olho_esquerdo = objetos[0]
olho_direito = objetos[1]

img = cv2.imread("hascas/rosto.png")
pts = np.array( [[olho_direito[0], olho_direito[1]],  [olho_direito[0], olho_direito[1]+olho_direito[3]], [olho_esquerdo[0]+[olho_esquerdo[2]], olho_esquerdo[1]+olho_esquerdo[3]], [olho_esquerdo[0]+[olho_esquerdo[2]], olho_esquerdo[1]]], np.int32)

# Cria uma máscara com os pontos
mask = np.zeros_like(img)
cv2.fillPoly(mask, [pts], (255, 255, 255))


# Aplica a máscara na imagem original
img_cortada = cv2.bitwise_and(img, mask)
part_cortada = cv2.bitwise_and(img, cv2.bitwise_not(mask))

cv2.imshow('Imagem cortada', part_cortada) #img #img_cortada #part_cortada
cv2.waitKey(0)
cv2.destroyAllWindows()
