#USA O rosto.png COMO EXEMPLO DE TESTE, ELE É MAIS COMO UMA BASE, É PARECIDO COM MUITAS DAS IMAGENS DA BASE QUE VAMOS USAR
import os
from os.path import join as pjoin

import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

classificador = cv2.CascadeClassifier(r"anexos/right_eye2.xml")
img = cv2.imread("IMAGENS-M/Rihanna-1-930x620.png")


imgGray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
# cv2.imshow('Imagem Cinza', imgGray)
objetos = classificador.detectMultiScale(imgGray, minSize=(90,90), scaleFactor=1.1, minNeighbors=10) # ou maxSize
print(objetos)

for x,y,l,a in objetos:
    pass
    cv2.rectangle(img,(x,y),(x+l,y+a),(255, 0, 0), 2)

# olho_esquerdo = objetos[1]
# olho_direito = objetos[0]

# # img = cv2.imread("hascas/rosto.png")
# pts = np.array( [[olho_direito[0], olho_direito[1]],  [olho_direito[0], olho_direito[1]+olho_direito[3]], [olho_esquerdo[0]+[olho_esquerdo[2]], olho_esquerdo[1]+olho_esquerdo[3]], [olho_esquerdo[0]+[olho_esquerdo[2]], olho_esquerdo[1]]], np.int32)

# # Cria uma máscara com os pontos
# mask = np.zeros_like(img)
# cv2.fillPoly(mask, [pts], (255, 255, 255))


# # Aplica a máscara na imagem original
# img_cortada = cv2.bitwise_and(img, mask)
# part_cortada = cv2.bitwise_and(img, cv2.bitwise_not(mask))






# Converta a imagem para o formato RGB para exibição com matplotlib
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img_cortada = cv2.cvtColor(img_cortada, cv2.COLOR_BGR2RGB)
# part_cortada = cv2.cvtColor(part_cortada, cv2.COLOR_BGR2RGB)




plt.imshow(img)
# plt.imshow(img_cortada)
# plt.imshow(part_cortada)
plt.axis('off')
plt.show()








# Melhores hass

# olhos = right_eye2