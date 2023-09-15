import threading
import time
import tkinter as tk
from tkinter import ttk


def iniciar_processamento(valor):
    progress_bar["value"] += valor 
    progress_bar.update()


# Cria a janela principal
janela = tk.Tk()
janela.title("ProgressBar")

# Cria a ProgressBar
progress_bar = ttk.Progressbar(janela, mode="determinate", maximum=100)
progress_bar.pack(padx=20, pady=20)

# Botão para iniciar o processamento
iniciar_button = tk.Button(janela, text="Iniciar Processamento", command=iniciar_processamento(10))
iniciar_button.pack(padx=20, pady=10)

# Iniciar a janela principal
janela.mainloop()