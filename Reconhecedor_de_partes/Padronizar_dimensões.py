import os

from PIL import Image

genero = "M"


tamanho = 0

imagens = os.listdir(f"IMAGENS-{genero}")
for imgi in imagens:
    img_verifica_dimensao = Image.open(f"IMAGENS-{genero}/{imgi}")
    # tranforma o tamanho da imagem, (redimensiona)
    tamanho_atualizado = img_verifica_dimensao.height
    if tamanho_atualizado > tamanho:
        tamanho = tamanho_atualizado
        dimensão_width = img_verifica_dimensao.width
        dimensão_height = img_verifica_dimensao.height

for imgi in imagens:
    img_dimensao = Image.open(f"IMAGENS-{genero}/{imgi}")
    img_resized = img_dimensao.resize((dimensão_width, dimensão_height))
    #salva
    img_resized.save(f"IMAGENS-{genero}/{imgi}")
    