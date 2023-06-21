import cv2
import numpy as np

# Carrega a imagem
img = cv2.imread('Image.ExportImages.0_.png')

# Define os pontos dos vértices
pts = np.array( [[120, 260],[120, 170],[370, 170],[370, 260], [290, 260], [290, 320], [310, 320], [310, 375], [160, 375], [160, 260]], np.int32)

# Cria uma máscara com os pontos
mask = np.zeros_like(img)
cv2.fillPoly(mask, [pts], (255, 255, 255))

# Aplica a máscara na imagem original
img_cortada = cv2.bitwise_and(img, mask)
part_cortada = cv2.bitwise_and(img, cv2.bitwise_not(mask))

# Exibe a imagem triangular
# cv2.imshow('Imagem cortada', img_cortada)

# cv2.imwrite("as.png", img_cortada) 


# from PIL import Image

# img = Image.open("as.png")
# rgba = img.convert("RGBA")
# datas = rgba.getdata()

# newData = []
# for item in datas:
#     if item[0] == 0 and item[1] == 0 and item[2] == 0:  # finding black colour by its RGB value
#         # storing a transparent value when we find a black colour
#         newData.append((255, 255, 255, 0))
#     else:
#         newData.append(item)  # other colours remain unchanged

# rgba.putdata(newData)
# rgba.save("as.png", "PNG")


# cv2.imshow('Imagem Cortada', img_cortada)
cv2.imshow('Parte Cortada', part_cortada)
cv2.waitKey(0)
cv2.destroyAllWindows()





# ((0, 170, 457, 260)) 