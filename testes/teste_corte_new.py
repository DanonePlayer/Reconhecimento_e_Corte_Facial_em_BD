import shutil
import tkinter as tk
from tkinter import filedialog

class SuaClasse:
    def __init__(self):
        # Defina os caminhos das imagens
        self.rosto_salva = 'caminho/para/rosto.png'
        self.olhos_salva = 'caminho/para/olhos.png'
        self.nariz_salva = 'caminho/para/nariz.png'
        self.boca_salva = 'caminho/para/boca.png'

    def Salvar(self, pasta_destino):
        # Copie as imagens para a pasta de destino
        shutil.copy(self.rosto_salva, pasta_destino)
        shutil.copy(self.olhos_salva, pasta_destino)
        shutil.copy(self.nariz_salva, pasta_destino)
        shutil.copy(self.boca_salva, pasta_destino)

def selecionar_pasta_destino():
    pasta_destino = filedialog.askdirectory()
    if pasta_destino:
        minha_classe = SuaClasse()
        minha_classe.Salvar(pasta_destino)
        resultado_label.config(text=f"Imagens salvas em: {pasta_destino}")

# Crie uma janela tkinter
janela = tk.Tk()
janela.title("Selecione a Pasta de Destino")

# Crie um botão para selecionar a pasta de destino
selecionar_button = tk.Button(janela, text="Selecionar Pasta de Destino", command=selecionar_pasta_destino)
selecionar_button.pack(pady=20)

# Crie uma label para mostrar o resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# Inicie o loop da interface gráfica
janela.mainloop()