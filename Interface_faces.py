import tkinter as tk
from tkinter import SUNKEN, PhotoImage
from PIL import Image, ImageTk
# import os
# import recorte
# import extrair


class Interface_rostos:
    def __init__(self, master):
        self.janelaprincipal = master

        
        self.janelaprincipal.title("Rawn")
        self.janelaprincipal.configure()
        self.janelaprincipal.geometry("1280x720")
        self.janelaprincipal.resizable(width=False, height=False )



        self.espaço = tk.Label(self.janelaprincipal)
        self.espaço.grid(column=0, row=0, padx=115)

        self.espaço1 = tk.Label(self.janelaprincipal, width=60, height=10 )
        self.espaço1.grid(column=1, row=0)

        self.frm_direito = tk.Frame(self.janelaprincipal, width=321, height=380, bg="#44284c")
        self.frm_direito.grid(column=1, row=1, padx=40)

        self.imagem_d = (f"Rosto_Inicial.png")
        self.imagem_d_lbl = ImageTk.PhotoImage(Image.open(self.imagem_d))
        self.lbl_d = tk.Label(self.frm_direito, image=self.imagem_d_lbl, width=341, height= 400)
        self.lbl_d.pack()

        self.lbl_d.configure(image=self.imagem_d_lbl)
        self.lbl_d.image=self.imagem_d_lbl


        self.frm_esquerdo = tk.Frame(self.janelaprincipal, width=321, height=380, bg="#44284c")
        self.frm_esquerdo.grid(column=2, row=1)

        self.imagem_e_lbl = ImageTk.PhotoImage(Image.open(f"Rosto_Inicial.png"))
        self.lbl_e = tk.Label(self.frm_esquerdo, image=self.imagem_e_lbl, width=341, height= 400)
        self.lbl_e.pack()

        self.lbl_e.configure(image=self.imagem_e_lbl)
        self.lbl_e.image=self.imagem_e_lbl


        self.frm_seleção = tk.Frame(self.janelaprincipal, width=90, height=400)
        self.frm_seleção.grid(column=3, row=1, padx=60)


        self.button_gerar_img_and_word = tk.Button(self.espaço1, text="Gerar Img and Word", command="self.Gerador")
        self.button_gerar_img_and_word.place(x=1, y=1)

        self.button_gerar_corte = tk.Button(self.espaço1, text="Gerar Cortes", command="self.recortes")
        self.button_gerar_corte.place(x=220, y=1)


        self.button_login = tk.Button(self.frm_seleção, text="Específico" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0)
        self.button_login.place(x=1, y=1)


        self.button_login = tk.Button(self.frm_seleção, text="Todo Banco" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0)
        self.button_login.place(x=1, y=31)


        self.button_login = tk.Button(self.frm_seleção, text="Feminino" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0)
        self.button_login.place(x=1, y=101)

        self.button_login = tk.Button(self.frm_seleção, text="Masculino" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0)
        self.button_login.place(x=1, y=132)


        # self.button_login = tk.Button(self.frm_seleção, text="Asiático" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0)
        # self.button_login.place(x=1, y=202)

        # self.button_login = tk.Button(self.frm_seleção, text="Branco" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0)
        # self.button_login.place(x=1, y=233)


        # self.button_login = tk.Button(self.frm_seleção, text="Índio" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0)
        # self.button_login.place(x=1, y=264)


        # self.button_login = tk.Button(self.frm_seleção, text="Negro" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0)
        # self.button_login.place(x=1, y=295)


        # self.button_login = tk.Button(self.frm_seleção, text="Pardo" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0)
        # self.button_login.place(x=1, y=233)


        self.button_Rosto = tk.Button(self.frm_seleção, text="Rosto" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0, command="self.Rosto")
        self.button_Rosto.place(x=1, y=202)


        self.button_Olhos = tk.Button(self.frm_seleção, text="Olhos" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0, command="self.Olhos")
        self.button_Olhos.place(x=1, y=233)


        self.button_Nariz = tk.Button(self.frm_seleção, text="Nariz" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0, command="self.Nariz")
        self.button_Nariz.place(x=1, y=264)


        self.button_Boca = tk.Button(self.frm_seleção, text="Boca" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0, command="self.Boca")
        self.button_Boca.place(x=1, y=295)



        self.frm_salvamento = tk.Frame(self.janelaprincipal, width=90, height=400)
        self.frm_salvamento.grid(column=3, row=2, padx=10)



        self.button_login = tk.Button(self.frm_salvamento, text="Exportar" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0)
        self.button_login.place(x=1, y=1)


        self.button_login = tk.Button(self.frm_salvamento, text="Salvar" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0, command="self.Salvar")
        self.button_login.place(x=1, y=31)


        self.button_login = tk.Button(self.frm_salvamento, text="Carregar" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0)
        self.button_login.place(x=1, y=61)


        self.button_login = tk.Button(self.frm_salvamento, text="Novo" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0)
        self.button_login.place(x=1, y=91)



        
janela = tk.Tk()
Interface_rostos(janela)
janela.mainloop()
