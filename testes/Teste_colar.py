import tkinter as tk

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

def atualizar_imagem():
    fundo = Image.open(f"Rosto-M/Teste-1.png")
    fundo = fundo.resize((350, 400))
    nova_imagem = ImageTk.PhotoImage(fundo)
    canvas.itemconfig(img, image=nova_imagem)
    canvas.image = nova_imagem  # Mantenha uma referência à nova imagem


# Crie uma janela tkinter
janela = tk.Tk()
janela.title("Colocar e Mover Olhos e Boca")







# Abrir imagem frontal
img_front = "Olhos-M/Teste-1.png"

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




img_corte = Image.open(f"IMAGENS-M/Teste-1.png")
imagem_d = img_corte.resize((350, 400))
imagem_d_lbl = ImageTk.PhotoImage(imagem_d)



# Crie um canvas para a área de desenho
canvas = tk.Canvas(janela, width=400, height=400)
canvas.pack()

mg = canvas.create_image(0, 0, anchor="nw", image=imagem_d_lbl)i

botao_atualizar = tk.Button(janela, text="Atualizar Imagem", command=atualizar_imagem)
botao_atualizar.pack()









# Desenhe um círculo para representar um olho
olho1 = canvas.create_image(50, 50, anchor="nw", image=image_front)
# olho2 = canvas.create_oval(200, 50, 250, 100, fill="white")

# Desenhe uma forma para representar a boca
# boca = canvas.create_rectangle(100, 200, 200, 220, fill="red")

# Configurar eventos de arraste para os olhos e a boca
canvas.tag_bind(olho1, "<ButtonPress-1>", iniciar_arraste)
# canvas.tag_bind(olho2, "<ButtonPress-1>", iniciar_arraste)
# canvas.tag_bind(boca, "<ButtonPress-1>", iniciar_arraste)
canvas.tag_bind(olho1, "<B1-Motion>", arrastar)
# canvas.tag_bind(olho2, "<B1-Motion>", arrastar)
# canvas.tag_bind(boca, "<B1-Motion>", arrastar)
canvas.tag_bind(olho1, "<ButtonRelease-1>", parar_arraste)
# canvas.tag_bind(olho2, "<ButtonRelease-1>", parar_arraste)
# canvas.tag_bind(boca, "<ButtonRelease-1>", parar_arraste)

# Inicie a janela
janela.mainloop()




# width = (background.width - frontImage.width) // 2






    # def iniciar_arraste(self, event):
    #     self.x_inicial, self.y_inicial, self.item_selecionado
    #     self.item_selecionado = self.canvas.find_closest(event.x, event.y)[0]
    #     self.x_inicial, self.y_inicial = event.x, event.y

    # def arrastar(self, event):
    #     self.x_inicial, self.y_inicial
    #     if self.item_selecionado is not None:
    #     self.canvas.move(self.item_selecionado, event.x - self.x_inicial, event.y - self.y_inicial)
    #     self.x_inicial, self.y_inicial = event.x, event.y

    # def parar_arraste(self, event):
    #     self.item_selecionado
    #     self.item_selecionado = None

    # def atualizar_imagem(self):
    #     fundo = Image.open(f"Rosto-M/Teste-1.png")
    #     fundo = fundo.resize((350, 400))
    #     nova_imagem = ImageTk.PhotoImage(fundo)
    #     self.canvas.itemconfig(img, image=nova_imagem)
    #     self.canvas.image = nova_imagem  # Mantenha uma referência à nova imagem