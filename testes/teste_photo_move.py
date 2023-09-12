import tkinter as tk


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

# Crie um canvas para a área de desenho
canvas = tk.Canvas(janela, width=400, height=400)
canvas.pack()

# Desenhe um círculo para representar um olho
olho1 = canvas.create_oval(50, 50, 100, 100, fill="white")
olho2 = canvas.create_oval(200, 50, 250, 100, fill="white")

# Desenhe uma forma para representar a boca
boca = canvas.create_rectangle(100, 200, 200, 220, fill="red")

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

# Inicie a janela
janela.mainloop()