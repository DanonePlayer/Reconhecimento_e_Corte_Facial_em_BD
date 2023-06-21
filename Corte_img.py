from PIL import Image

# Imagem frontal
img_front = r"Nariz-M/m.png"
  
# Imagem de trás
img_back = r"Tronco-M/a.png"
  
# Abrir imagem frontal
frontImage = Image.open(img_front)
  
# Abrir imagem de fundo
background = Image.open(img_back)
  
# Converter imagem para RGBA
frontImage = frontImage.convert("RGBA")
  
# Converter imagem para RGBA
background = background.convert("RGBA")
  
# Calcula a largura para estar no centro
width = (background.width - frontImage.width) // 2
  
# Calcula a altura para estar no centro
height = (background.height - frontImage.height) // 2
  
# Cole o frontImage em (largura, altura)
background.paste(frontImage, (width, height), frontImage)
  

# background.show()



olho = Image.open(r"Olhos-M/c.png")
background.paste(olho, (85, 123))
# background.show()


boca = Image.open(r"Boca-M/d.png")
background.paste(boca, (112, 235))
background.show()





# # Save this image
# background.save("new.png", format="png")