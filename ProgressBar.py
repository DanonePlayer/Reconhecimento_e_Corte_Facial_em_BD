import tkinter as tk
from tkinter.ttk import Progressbar


def start():
    for i in range(0, 101):
        progress.set(i)
        print(i)
        bar.update_idletasks()

janela = tk.Tk()
janela.title("Ola mundo")
janela.geometry('350x200')

# style = ttk.Style()
# style.theme_use('default')
# style.configure("black.Horizontal.TProgressbar", background='black')
progress = tk.DoubleVar()
progress.set(0)

bar = Progressbar(janela, length=200, style='black.Horizontal.TProgressbar', variable=progress)
bar.grid(column=0, row=0)

startButton = tk.Button(janela, text='Iniciar', command=start)
startButton.grid(row=0, column=2)




janela.mainloop()