import os
import tkinter as tk
from tkinter import SUNKEN, PhotoImage

from PIL import Image, ImageTk

width = 350
height = 400

# Abrir imagem frontal
img_front = "Olhos-M/Teste-1.png"

# Abrir imagem de fundo
img_back = "Rosto-M/Teste-1.png"

frontImage = Image.open(img_front)
frontImage = frontImage.resize((width, height))
background = Image.open(img_back)
background = background.resize((width, height))

# Converter imagem para RGBA
frontImage = frontImage.convert("RGBA")
frontImage.show()
# Converter imagem para RGBA
background = background.convert("RGBA")

background.show()
# Calcula a largura para estar no centro
width = (background.width - frontImage.width) // 2

# Calcula a altura para estar no centro
height = (background.height - frontImage.height) // 2

# Cole o frontImage em (largura, altura)
background.paste(frontImage, (width, height), frontImage)

# imagem = ImageTk.PhotoImage(background)

# self.Rosto_salva = background

# self.image_label2.configure(image=imagem)
# self.image_label2.image=imagem
# self.janela2.destroy()