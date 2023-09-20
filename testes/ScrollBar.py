import tkinter as tk
from tkinter import ttk

# def on_scroll(*args):
#     canvas.yview(*args)
    
root = tk.Tk()
root.title("Exemplo de Scrollbar")

# Crie um frame para conter os labels
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Crie um canvas dentro do frame
canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Adicione uma barra de rolagem vertical ao canvas
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Crie outro frame dentro do canvas
content_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=content_frame, anchor=tk.NW)

background_label = ttk.Label(content_frame, background='blue', text="")
background_label.pack(fill=tk.BOTH, expand=True)

# Adicione os labels ao content_frame (substitua isso com seus próprios labels)
for i in range(20):
    label = ttk.Label(content_frame, text=f"Label {i}")
    label.pack(fill=tk.X)

# Atualize a região de rolagem quando o tamanho do content_frame mudar
content_frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

# Permita que o usuário role a janela
canvas.bind_all("<MouseWheel>", lambda event, canvas=canvas: canvas.yview_scroll(-1 * (event.delta // 120), "units"))

root.mainloop()