# import time

# from tqdm import tqdm

# # Número total de iterações
# total_iteracoes = 100

# # Crie uma barra de carregamento usando tqdm
# for i in tqdm(range(total_iteracoes), desc="Processando", ncols=100):
#     # Simule uma tarefa demorada
#     time.sleep(0.1)

# print("Tarefa concluída!")

from time import sleep
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar


def start():
    for i in range(0, 101):
        progress.set(i)
        sleep(0.1)
        print(i)
        bar.update_idletasks()

janela = Tk()
janela.title("Ola mundo")
janela.geometry('350x200')

# style = ttk.Style()
# style.theme_use('default')
# style.configure("black.Horizontal.TProgressbar", background='black')
progress = DoubleVar()
progress.set(0)

bar = Progressbar(janela, length=200, style='black.Horizontal.TProgressbar', variable=progress)
bar.grid(column=0, row=0)

startButton = Button(janela, text='Iniciar', command=start)
startButton.grid(row=0, column=2)




janela.mainloop()