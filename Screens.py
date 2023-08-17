##from PIL import Image, ImageTk
import tkinter as tk
from tkinter import SUNKEN, PhotoImage



class Interface:
    def __init__(self, master):
        self.main = master
        self.main.title('Programa de Recorte e Reconhecimento Facial.exe')
        self.main.geometry("1580x920")
        ##self.main.resizable(width=False, height=False)
        self.main.configure(bg='#8F8B8B')
        #self.main.attributes('-fullscreen', True)


        self.frm_left = tk.Frame(self.main, bg='#474444', width=150, height=720)
        self.frm_left.pack(side=tk.LEFT, fill=tk.Y)


        ##Funções 01

        self.lbl_01 = tk.Label(self.frm_left,text="MENU",font=('Lato',16,'bold'), fg='#FFF', bg='#474444')
        self.lbl_01.grid(row=0, column=0, padx=30, pady=(30, 5))

        btn = tk.Button(self.frm_left,width=15,height=1, bg='#D9D9D9',borderwidth=0, text='Word', font=('Arial',10,'bold'), fg='#474444', command='')
        btn.grid(row=1, column=0, padx=30, pady=(30, 5))

        btn_01 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9',borderwidth=0, text='Corte', font=('Arial',10,'bold'), fg='#474444', command='')
        btn_01.grid(row=2, column=0, padx=30, pady=5)

        ##Funções02

        btn_02 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9',borderwidth=0, text='Especifico', font=('Arial',10,'bold'), fg='#474444',command='')
        btn_02.grid(row=3, column=0, padx=30, pady=(30, 5))

        btn_03 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9',borderwidth=0, text='Todo Branco', font=('Arial',10,'bold'), fg='#474444',command='')
        btn_03.grid(row=4, column=0, padx=30, pady=5)

        ##Funções03

        btn_04 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9',borderwidth=0, text='Rosto', font=('Arial',10,'bold'), fg='#474444',command='')
        btn_04.grid(row=5, column=0, padx=30, pady=(30, 5))

        btn_05 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9',borderwidth=0, text='Olhos', font=('Arial',10,'bold'), fg='#474444', command='')
        btn_05.grid(row=6, column=0, padx=30, pady=5)

        btn_06 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9',borderwidth=0, text='Nariz', font=('Arial',10,'bold'), fg='#474444',command='')
        btn_06.grid(row=7, column=0, padx=30, pady=5)

        btn_07 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9',borderwidth=0, text='Boca', font=('Arial',10, 'bold'), fg='#474444',command='')
        btn_07.grid(row=8, column=0, padx=30, pady=5)

        #Funções_04

        btn_08 = tk.Button(self.frm_left, width=15, height=1, bg='#969696',borderwidth=0, text='Masculino', font=('Arial',10, 'bold'), fg='#fff',command='')
        btn_08.grid(row=9, column=0, padx=30, pady=(30, 5))

        btn_09 = tk.Button(self.frm_left, width=15, height=1, bg='#969696',borderwidth=0, text='Feminino', font=('Arial',10, 'bold'), fg='#fff',command='')
        btn_09.grid(row=10, column=0, padx=30, pady=5)

        #Funções_05

        btn_10 = tk.Button(self.frm_left, width=15, height=1, bg='#5B5A5A', borderwidth=0, text='Exportar', font=('Arial',10, 'bold'), fg='#fff',command='')
        btn_10.grid(row=11, column=0, padx=30, pady=(30, 5))

        btn_11 = tk.Button(self.frm_left, width=15, height=1, bg='#5B5A5A', borderwidth=0, text='Salvar', font=('Arial',10, 'bold'), fg='#fff',command='')
        btn_11.grid(row=12, column=0, padx=30, pady=5)

        btn_12 = tk.Button(self.frm_left, width=15, height=1, bg='#5B5A5A', borderwidth=0, text='Carregar', font=('Arial',10, 'bold'), fg='#fff',command='')
        btn_12.grid(row=13, column=0, padx=30, pady=5)

        btn_13 = tk.Button(self.frm_left, width=15, height=1, bg='#5B5A5A', borderwidth=0, text='Novo', font=('Arial',10, 'bold'), fg='#fff',command='')
        btn_13.grid(row=14, column=0, padx=30, pady=5)

        btn_14 = tk.Button(self.frm_left, width=15, height=1, bg='#5B5A5A', borderwidth=0, text='Sair', font=('Arial', 10, 'bold'), fg='#fff', command=self.Sair)
        btn_14.grid(row=15, column=0, padx=30, pady=5)



        self.frm_left.pack_propagate(False)

        self.frm_center = tk.Frame(self.main)
        self.frm_center.pack(side=tk.LEFT,fill=tk.BOTH,padx=(40,20),pady=40,expand=True)


        self.frm_center_main = tk.Frame(self.frm_center, bg='#303030')
        self.frm_center_main.pack(fill=tk.BOTH, expand=True)


        self.label_programa = tk.Label(self.frm_center_main, text="PROGRAMA DE RECORTE E RECONHECIMENTO", font=('Roboto', 20), bg='#303030',fg='white')
        self.label_programa.pack(pady=(50, 0))

        self.label_versao = tk.Label(self.frm_center_main, text="Versão ALFA", font=('Roboto', 16), bg='#303030', fg='white')
        self.label_versao.pack(pady=(0, 40))



        self.image_label1 = tk.Label(self.frm_center_main, bg='white', width=41, height= 30)
        self.image_label1.pack(padx=50, pady=(10,70),side=tk.LEFT,fill=tk.BOTH)

        self.image_label2 = tk.Label(self.frm_center_main, bg='white',width=41, height= 30)
        self.image_label2.pack(padx=50, pady=(10,70),side=tk.RIGHT,fill=tk.BOTH)

        self.label_imagem_original = tk.Label(self.frm_center_main, text="IMAGEM ORIGINAL", bg='#303030', fg='white',width=51, height= 40)
        self.label_imagem_original.pack(in_=self.image_label1, pady=(0, 5))

        self.btn = tk.Button(self.image_label1, text='Miniatura',borderwidth=0,font=('Arial',14, 'bold'), fg='#fff',bg='#5B5A5A')
        self.btn.pack(side=tk.BOTTOM,expand=True,pady=(0, 5))

        self.label_recorde = tk.Label(self.frm_center_main, text="RECORTE", bg='#303030', fg='white',width=51, height= 40)
        self.label_recorde.pack(in_=self.image_label2, pady=(0, 5))

        self.btn2 = tk.Button(self.image_label2, text='Limpar', borderwidth=0, font=('Arial', 14, 'bold'), fg='#fff',bg='#5B5A5A')
        self.btn2.pack(side=tk.BOTTOM, expand=True, pady=(0, 5))

        self.frm_bottom = tk.Frame(self.main, bg='#303030')
        self.frm_bottom.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH, padx=20, pady=20)

        self.label_image = tk.Label(self.frm_center_main, text="RECORTE", bg='#303030', fg='white',width=51, height= 40)
        self.label_recorde.pack(in_=self.image_label2, pady=(0, 5))


        image_labels = []
        clear_buttons = []

        for i in range(4):
            label = tk.Label(self.frm_bottom, bg='white',height=10,width=20)
            label.pack(side=tk.TOP, padx=30,pady=10,expand=True,fill=tk.BOTH)

            label_image = tk.Label(self.frm_bottom, text="RECORTE", bg='#303030', fg='white', width=20,height=10)
            label_image.pack(in_=label)

            clear_button = tk.Button(self.frm_bottom, text='Limpar',borderwidth=0,font=('Arial',10, 'bold'), fg='#fff',bg='#5B5A5A')
            clear_button.pack(side=tk.TOP, padx=10,pady=7,)
            clear_buttons.append(clear_button)

    def Sair(self):
        self.main.destroy()


janela = tk.Tk()
Interface(janela)
janela.mainloop()

