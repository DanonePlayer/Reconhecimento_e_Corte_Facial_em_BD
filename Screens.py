import tkinter as tk
from tkinter import SUNKEN, PhotoImage
from PIL import Image, ImageTk
import os

class Interface:
    def __init__(self, master):
        self.main = master
        self.main.title('Tela Principal')
        self.main.geometry("1280x720")
        self.main.resizable(width=False, height=False)

        self.frm_left = tk.Frame(self.main, bg='#474444', width=150, height=720)
        self.frm_left.pack(side=tk.LEFT, fill=tk.Y)


        ##Funções 01

        btn = tk.Button(self.frm_left,width=15,height=1, bg='#D9D9D9',borderwidth=0)
        btn.grid(row=0, column=0, padx=30, pady=(30, 5))

        btn_01 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9',borderwidth=0)
        btn_01.grid(row=1, column=0, padx=30, pady=5)

        ##Funções02

        btn_02 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9',borderwidth=0)
        btn_02.grid(row=2, column=0, padx=30, pady=(30, 5))

        btn_03 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9',borderwidth=0)
        btn_03.grid(row=3, column=0, padx=30, pady=5)

        ##Funções03

        btn_04 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9',borderwidth=0)
        btn_04.grid(row=4, column=0, padx=30, pady=(30, 5))

        btn_05 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9',borderwidth=0)
        btn_05.grid(row=5, column=0, padx=30, pady=5)

        btn_06 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9',borderwidth=0)
        btn_06.grid(row=6, column=0, padx=30, pady=5)

        btn_07 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9',borderwidth=0)
        btn_07.grid(row=7, column=0, padx=30, pady=5)

        #Funcções_04

        btn_08 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9',borderwidth=0)
        btn_08.grid(row=8, column=0, padx=30, pady=(30, 5))

        btn_09 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9',borderwidth=0)
        btn_09.grid(row=9, column=0, padx=30, pady=5)

        #Funções_05

        btn_10 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9', borderwidth=0)
        btn_10.grid(row=10, column=0, padx=30, pady=(30, 5))

        btn_11 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9', borderwidth=0)
        btn_11.grid(row=11, column=0, padx=30, pady=5)

        btn_12 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9', borderwidth=0)
        btn_12.grid(row=12, column=0, padx=30, pady=5)

        btn_13 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9', borderwidth=0)
        btn_13.grid(row=13, column=0, padx=30, pady=5)



        self.frm_left.pack_propagate(False)

        self.frm_center = tk.Frame(self.main)
        self.frm_center.pack(side=tk.LEFT, expand=True,fill=tk.BOTH,padx=40,pady=40)


        self.frm_center_main = tk.Frame(self.frm_center, bg='#303030')
        self.frm_center_main.pack(fill=tk.BOTH, expand=True)


        self.label_programa = tk.Label(self.frm_center_main, text="PROGRAMA DE RECORTE E RECONHECIMENTO", font=('Arial', 20), bg='#303030',fg='white')
        self.label_programa.pack(pady=(50, 0))

        self.label_versao = tk.Label(self.frm_center_main, text="Versão BETA", font=('Arial', 16), bg='#303030', fg='white')
        self.label_versao.pack(pady=(0, 40))


        self.image_label1 = tk.Label(self.frm_center_main, bg='white', width=41, height= 30)
        self.image_label1.pack(padx=50, pady=(10,70),side=tk.LEFT)

        self.image_label2 = tk.Label(self.frm_center_main, bg='white',width=41, height= 30)
        self.image_label2.pack(padx=50, pady=(10,70),side=tk.RIGHT)

        self.label_imagem_original = tk.Label(self.frm_center_main, text="IMAGEM ORIGINAL", bg='#303030', fg='white',width=41, height= 30)
        self.label_imagem_original.pack(in_=self.image_label1, pady=(0, 5))

        self.label_recorde = tk.Label(self.frm_center_main, text="RECORTE", bg='#303030', fg='white',width=41, height= 30)
        self.label_recorde.pack(in_=self.image_label2, pady=(0, 5))

janela = tk.Tk()
Interface(janela)
janela.mainloop()
