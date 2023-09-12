import os
from os.path import join as pjoin

import cv2
import numpy as np
from PIL import Image

Image1 = Image.open(f"IMAGENS-M/Teste-1.png") 
croppedIm = Image1.crop((256, 404, 766, 561)) 
croppedIm.show()
# path_to_file = pjoin(f"Olhos-{genero}",imgi)
# croppedIm.save(path_to_file)


# [[256, 404], [256, 566], [766, 561], [766, 404]]
# croppedIm = Image1.crop((404, 256, 766, 561)) 