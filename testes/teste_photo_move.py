import os
import tkinter as tk
from tkinter import SUNKEN, PhotoImage

from PIL import Image, ImageTk


def iniciar_arraste(event):
    global x_inicial, y_inicial, item_selecionado
    item_selecionado = canvas.find_closest(event.x, event.y)[0]
    x_inicial, y_inicial = event.x, event.y

def arrastar(event):
    global x_inicial, y_inicial
    if item_selecionado is not None:
        canvas.move(item_selecionado, event.x - x_inicial, event.y - y_inicial)
        x_inicial, y_inicial = event.x, event.y

def parar_arraste(event):
    global item_selecionado
    item_selecionado = None

# Crie uma janela tkinter
janela = tk.Tk()
janela.title("Colocar e Mover Olhos e Boca")

# Abrir imagem frontal
img_front = "IMAGENS-M/Teste-1.png"

# Abrir imagem de fundo
img_back = "IMAGENS-M/Teste-1.png"

frontImage = Image.open(img_front)
frontImage = frontImage.resize((350, 400))
background = Image.open(img_back)
background = background.resize((350, 400))

# Converter imagem para RGBA
frontImage = frontImage.convert("RGBA")

# Converter imagem para RGBA
background = background.convert("RGBA")
image_front = ImageTk.PhotoImage(frontImage)

# Crie um canvas para a área de desenho
canvas = tk.Canvas(janela, width=400, height=400)
canvas.pack()

# Desenhe um círculo para representar um olho
olho1 = canvas.create_image(50, 50, anchor="nw", image=image_front)
olho2 = canvas.create_image(50, 50, anchor="nw", image=image_front)

# Desenhe uma forma para representar a boca
boca = canvas.create_image(50, 50, anchor="nw", image=image_front)

# Configurar eventos de arraste para os olhos e a boca
canvas.tag_bind(olho1, "<ButtonPress-1>", iniciar_arraste)
canvas.tag_bind(olho2, "<ButtonPress-1>", iniciar_arraste)
canvas.tag_bind(boca, "<ButtonPress-1>", iniciar_arraste)
canvas.tag_bind(olho1, "<B1-Motion>", arrastar)
canvas.tag_bind(olho2, "<B1-Motion>", arrastar)
canvas.tag_bind(boca, "<B1-Motion>", arrastar)
canvas.tag_bind(olho1, "<ButtonRelease-1>", parar_arraste)
canvas.tag_bind(olho2, "<ButtonRelease-1>", parar_arraste)
canvas.tag_bind(boca, "<ButtonRelease-1>", parar_arraste)

# Dicionário para rastrear imagens carregadas
imagens_carregadas = {olho1: frontImage, olho2: frontImage, boca: frontImage}

def salvar_imagem():
    resultado = Image.new("RGBA", (400, 400), (255, 255, 255, 255))

    for item in canvas.find_all():
        if canvas.type(item) == "image":
            image = imagens_carregadas.get(item)
            if image:
                x0, y0 = canvas.coords(item)
                resultado.paste(image, (int(x0), int(y0)))

    resultado.save("imagem_resultante.png")
    print("Imagem salva como imagem_resultante.png")

# Crie um botão para salvar a imagem
botao_salvar = tk.Button(janela, text="Salvar Imagem", command=salvar_imagem)
botao_salvar.pack()

# Inicie a janela
janela.mainloop()