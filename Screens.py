# flake8: noqa
import os
import tkinter as tk
from tkinter import SUNKEN, PhotoImage

from PIL import Image, ImageTk


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

        btn_04 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9', borderwidth=0, text='Rosto', font=('Arial',10,'bold'), fg='#474444', command=self.Rosto)
        btn_04.grid(row=5, column=0, padx=30, pady=(30, 5))

        btn_05 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9', borderwidth=0, text='Olhos', font=('Arial',10,'bold'), fg='#474444', command=self.Olhos)
        btn_05.grid(row=6, column=0, padx=30, pady=5)

        btn_06 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9', borderwidth=0, text='Nariz', font=('Arial',10,'bold'), fg='#474444', command=self.Nariz)
        btn_06.grid(row=7, column=0, padx=30, pady=5)

        btn_07 = tk.Button(self.frm_left, width=15, height=1, bg='#D9D9D9', borderwidth=0, text='Boca', font=('Arial',10, 'bold'), fg='#474444', command=self.Boca)
        btn_07.grid(row=8, column=0, padx=30, pady=5)

        #Funções_04

        btn_08 = tk.Button(self.frm_left, width=15, height=1, bg='#969696', borderwidth=0, text='Masculino', font=('Arial',10, 'bold'), fg='#fff', command='')
        btn_08.grid(row=9, column=0, padx=30, pady=(30, 5))

        btn_09 = tk.Button(self.frm_left, width=15, height=1, bg='#969696', borderwidth=0, text='Feminino', font=('Arial',10, 'bold'), fg='#fff', command='')
        btn_09.grid(row=10, column=0, padx=30, pady=5)

        #Funções_05

        btn_10 = tk.Button(self.frm_left, width=15, height=1, bg='#5B5A5A', borderwidth=0, text='Exportar', font=('Arial',10, 'bold'), fg='#fff', command='')
        btn_10.grid(row=11, column=0, padx=30, pady=(30, 5))

        btn_11 = tk.Button(self.frm_left, width=15, height=1, bg='#5B5A5A', borderwidth=0, text='Salvar', font=('Arial',10, 'bold'), fg='#fff', command='')
        btn_11.grid(row=12, column=0, padx=30, pady=5)

        btn_12 = tk.Button(self.frm_left, width=15, height=1, bg='#5B5A5A', borderwidth=0, text='Carregar', font=('Arial',10, 'bold'), fg='#fff', command='')
        btn_12.grid(row=13, column=0, padx=30, pady=5)

        btn_13 = tk.Button(self.frm_left, width=15, height=1, bg='#5B5A5A', borderwidth=0, text='Novo', font=('Arial',10, 'bold'), fg='#fff', command='')
        btn_13.grid(row=14, column=0, padx=30, pady=5)

        btn_14 = tk.Button(self.frm_left, width=15, height=1, bg='#5B5A5A', borderwidth=0, text='Sair', font=('Arial', 10, 'bold'), fg='#fff', command=self.Sair)
        btn_14.grid(row=15, column=0, padx=30, pady=5)

        self.frm_left.pack_propagate(False)

        self.frm_center = tk.Frame(self.main)
        self.frm_center.pack(side=tk.LEFT,fill=tk.BOTH,padx=(40,20),pady=40,expand=True)

        self.frm_center_main = tk.Frame(self.frm_center, bg='#303030')
        self.frm_center_main.pack(fill=tk.BOTH, expand=True,side=tk.TOP)

        self.label_programa = tk.Label(self.frm_center_main, text="PROGRAMA DE RECORTE E RECONHECIMENTO", font=('Roboto', 20), bg='#303030',fg='white')
        self.label_programa.pack(pady=(50, 0))

        self.label_versao = tk.Label(self.frm_center_main, text="Versão ALFA", font=('Roboto', 16), bg='#303030', fg='white')
        self.label_versao.pack(pady=(0, 40))

        img_image_label1 = Image.open(f"Images_Interface/Rosto_inicial.png")
        self.img_image_label1_corte = img_image_label1.resize((350, 400))
        self.img_image_label1_e = ImageTk.PhotoImage(self.img_image_label1_corte)
        self.image_label1 = tk.Label(self.frm_center_main, image=self.img_image_label1_e, bg='white', width=350, height= 400)
        self.image_label1.pack(padx=50, pady=(10,5),side=tk.LEFT)
        self.image_label1.configure(image=self.img_image_label1_e)
        self.image_label1.image=self.img_image_label1_e

        img_image_label2 = Image.open(f"Images_Interface/Rosto_inicial.png")
        self.img_image_label2_corte = img_image_label2.resize((350, 400))
        self.img_image_label2_d = ImageTk.PhotoImage(self.img_image_label2_corte)
        self.image_label2 = tk.Label(self.frm_center_main, image=self.img_image_label2_d, width=350, height= 400)
        self.image_label2.pack(padx=50, pady=(10,5),side=tk.RIGHT)
        self.image_label2.configure(image=self.img_image_label2_d)
        self.image_label2.image=self.img_image_label2_d

        self.frame_down = tk.Frame(self.frm_center, bg='#303030')
        self.frame_down.pack(fill=tk.BOTH, expand=True,side=tk.TOP)
        self.btn = tk.Button(self.frame_down, text='Miniatura',borderwidth=0,font=('Arial',12, 'bold'), fg='#fff',bg='#5B5A5A', command=self.gerar_miniatura)
        self.btn.pack(side=tk.LEFT,expand=True,pady=(0, 10),padx=50)
        self.btn2 = tk.Button(self.frame_down, text='Limpar', borderwidth=0, font=('Arial', 12, 'bold'), fg='#fff',bg='#5B5A5A')
        self.btn2.pack(side=tk.RIGHT, expand=True, pady=(0, 10),padx=50)


        img_image_miniatura = Image.open(f"Images_Interface/Rosto_inicial.png")
        self.image_miniatura_corte = img_image_miniatura.resize((110, 130))
        self.image_miniatura = ImageTk.PhotoImage(self.image_miniatura_corte)

        img_botão_adiciona_miniatura = Image.open(f"Images_Interface/adicionar-botao.png")
        self.botão_adiciona_miniatura_corte = img_botão_adiciona_miniatura.resize((28,28))
        self.botão_adiciona_miniatura = ImageTk.PhotoImage(self.botão_adiciona_miniatura_corte)

        self.baixo1 = False
        self.baixo2 = False
        self.baixo3 = False
        self.baixo4 = False

        self.frm_bottom = tk.Frame(self.main, bg='#303030')
        self.frm_bottom.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH, padx=20, pady=20)

        self.Miniatura_01 = tk.Label(self.frm_bottom, bg='#474444',image=self.image_miniatura)
        self.Miniatura_01.pack(side=tk.TOP, padx=30,pady=10, expand=True)
        self.frame_bttn_01 = tk.Frame(self.frm_bottom,bg='#303030')
        self.frame_bttn_01.pack(side=tk.TOP, padx=10,pady=7,)
        add_button_01 = tk.Button(self.frame_bttn_01,image=self.botão_adiciona_miniatura, fg='#fff',bg='#5B5A5A',borderwidth=0)
        add_button_01.pack(side=tk.RIGHT, padx=10, pady=7,expand=True)
        clear_button_01 = tk.Button(self.frame_bttn_01, text='Limpar',borderwidth=0,font=('Arial',10, 'bold'), fg='#fff',bg='#5B5A5A', command=lambda: self.excluir_miniaturas(1))
        clear_button_01.pack(side=tk.LEFT, padx=10,pady=7,)

        self.Miniatura_02 = tk.Label(self.frm_bottom, bg='#474444', image=self.image_miniatura)
        self.Miniatura_02.pack(side=tk.TOP, padx=30, pady=10, expand=True)
        self.frame_bttn_02 = tk.Frame(self.frm_bottom, bg='#303030')
        self.frame_bttn_02.pack(side=tk.TOP, padx=10, pady=7, )
        clear_button_02 = tk.Button(self.frame_bttn_02, text='Limpar', borderwidth=0, font=('Arial', 10, 'bold'),fg='#fff', bg='#5B5A5A', command=lambda: self.excluir_miniaturas(2))
        clear_button_02.pack(side=tk.LEFT, padx=10, pady=7, )
        add_button_02 = tk.Button(self.frame_bttn_02, image=self.botão_adiciona_miniatura, fg='#fff', bg='#5B5A5A', borderwidth=0)
        add_button_02.pack(side=tk.RIGHT, padx=10, pady=7, expand=True)

        self.Miniatura_03 = tk.Label(self.frm_bottom, bg='#474444', image=self.image_miniatura)
        self.Miniatura_03.pack(side=tk.TOP, padx=30, pady=10, expand=True)
        self.frame_bttn_03 = tk.Frame(self.frm_bottom, bg='#303030')
        self.frame_bttn_03.pack(side=tk.TOP, padx=10, pady=7, )
        clear_button_03 = tk.Button(self.frame_bttn_03, text='Limpar', borderwidth=0, font=('Arial', 10, 'bold'),fg='#fff', bg='#5B5A5A', command=lambda: self.excluir_miniaturas(3))
        clear_button_03.pack(side=tk.LEFT, padx=10, pady=7, )
        add_button_03 = tk.Button(self.frame_bttn_03, image=self.botão_adiciona_miniatura, fg='#fff', bg='#5B5A5A', borderwidth=0)
        add_button_03.pack(side=tk.RIGHT, padx=10, pady=7, expand=True)

        self.Miniatura_04 = tk.Label(self.frm_bottom, bg='#474444', image=self.image_miniatura)
        self.Miniatura_04.pack(side=tk.TOP, padx=30, pady=10, expand=True)
        self.frame_bttn_04 = tk.Frame(self.frm_bottom, bg='#303030')
        self.frame_bttn_04.pack(side=tk.TOP, padx=10, pady=7, )
        clear_button_04 = tk.Button(self.frame_bttn_04, text='Limpar', borderwidth=0, font=('Arial', 10, 'bold'),fg='#fff', bg='#5B5A5A', command=lambda: self.excluir_miniaturas(4))
        clear_button_04.pack(side=tk.LEFT, padx=10, pady=7, )
        add_button_04 = tk.Button(self.frame_bttn_04, image=self.botão_adiciona_miniatura, fg='#fff', bg='#5B5A5A', borderwidth=0)
        add_button_04.pack(side=tk.RIGHT, padx=10, pady=7, expand=True)

        self.Miniatura_01.configure(image=self.image_miniatura)
        self.Miniatura_01.image=self.image_miniatura
        self.Miniatura_02.configure(image=self.image_miniatura)
        self.Miniatura_02.image=self.image_miniatura
        self.Miniatura_03.configure(image=self.image_miniatura)
        self.Miniatura_03.image=self.image_miniatura
        self.Miniatura_04.configure(image=self.image_miniatura)
        self.Miniatura_04.image=self.image_miniatura

        self.começa = 0
        self.termina = 6

    def Sair(self):
        self.main.destroy()

    def Gerador(self):
        "extrair.Gerador_imagens()"

    def recortes(self):
        'recorte.recortes("M")'
        'recorte.recortes("F")'

    def Rosto(self):
        Parte = "Rosto"
        self.ImgsClick(Parte)

    def Nariz(self):
        Parte = "Nariz"
        self.ImgsClick(Parte)

    def Boca(self):
        Parte = "Boca"
        self.ImgsClick(Parte)

    def Olhos(self):
        Parte = "Olhos"
        self.ImgsClick(Parte)

    def StartImgs(self, Parte):           
        rostos = os.listdir(f"IMAGENS-M")
        self.vetor_rostos = []
        for rosto in range(self.começa, self.termina):
            self.vetor_rostos.append(rostos[rosto])
        # print(self.vetor_rostos)

        self.width = 350
        self.height = 400

        image1 = (Image.open(f"{Parte}-M/{self.vetor_rostos[0]}"))
        image1 = image1.resize((self.width, self.height))
        self.imagem1 = ImageTk.PhotoImage(image1)
        self.arq_Image_1 = (f"{Parte}-M/{self.vetor_rostos[0]}")
        image2 = (Image.open(f"{Parte}-M/{self.vetor_rostos[1]}"))
        image2 = image2.resize((self.width, self.height))
        self.imagem2 = ImageTk.PhotoImage(image2)
        self.arq_Image_2 = (f"{Parte}-M/{self.vetor_rostos[1]}")
        image3 = (Image.open(f"{Parte}-M/{self.vetor_rostos[2]}"))
        image3 = image3.resize((self.width, self.height))
        self.imagem3 = ImageTk.PhotoImage(image3)
        self.arq_Image_3 = (f"{Parte}-M/{self.vetor_rostos[2]}")
        image4 = (Image.open(f"{Parte}-M/{self.vetor_rostos[3]}"))
        image4 = image4.resize((self.width, self.height))
        self.imagem4 = (ImageTk.PhotoImage(image4))
        self.arq_Image_4 = (f"{Parte}-M/{self.vetor_rostos[3]}")
        image5 = (Image.open(f"{Parte}-M/{self.vetor_rostos[4]}"))
        image5 = image5.resize((self.width, self.height))
        self.imagem5 = ImageTk.PhotoImage(image5)
        self.arq_Image_5 = (f"{Parte}-M/{self.vetor_rostos[4]}")
        image6 = (Image.open(f"{Parte}-M/{self.vetor_rostos[5]}"))
        image6 = image6.resize((self.width, self.height))
        self.imagem6 = ImageTk.PhotoImage(image6)
        self.arq_Image_6 = (f"{Parte}-M/{self.vetor_rostos[5]}")


    def ImgsClick(self, Parte):
        self.StartImgs(Parte)

        self.janela2 = tk.Toplevel()
        self.janela2.title(Parte)
        self.janela2.resizable(width=False, height=False)


        self.frm_rosto1 = tk.Frame(self.janela2, width=321, height=380, bg="#44284c")
        self.frm_rosto1.grid(column=0, row=0)
        self.lbl_rosto1 = tk.Label(self.frm_rosto1, image=self.imagem1, width=341, height= 400)
        self.lbl_rosto1.bind("<Button-1>", lambda argumento_necesario = self.imagem1: self.Click_Photo(self.imagem1, Parte, self.arq_Image_1))
        self.lbl_rosto1.pack()



        self.frm_rosto2 = tk.Frame(self.janela2, width=321, height=380, bg="#6A5ACD")
        self.frm_rosto2.grid(column=0, row=1)
        self.lbl_rosto2 = tk.Label(self.frm_rosto2, image=self.imagem2, width=341, height= 400)
        self.lbl_rosto2.bind("<Button-1>", lambda argumento_necesario = self.imagem1: self.Click_Photo(self.imagem2, Parte, self.arq_Image_2))
        self.lbl_rosto2.pack()



        self.frm_rosto3 = tk.Frame(self.janela2, width=321, height=380, bg="#87CEFA")
        self.frm_rosto3.grid(column=1, row=0)
        self.lbl_rosto3 = tk.Label(self.frm_rosto3, image=self.imagem3, width=341, height= 400)
        self.lbl_rosto3.bind("<Button-1>", lambda argumento_necesario = self.imagem1: self.Click_Photo(self.imagem3, Parte, self.arq_Image_3))
        self.lbl_rosto3.pack()



        self.frm_rosto4 = tk.Frame(self.janela2, width=321, height=380, bg="#00FF7F")
        self.frm_rosto4.grid(column=1, row=1)
        self.lbl_rosto4 = tk.Label(self.frm_rosto4, image=self.imagem4, width=341, height= 400)
        self.lbl_rosto4.bind("<Button-1>", lambda argumento_necesario = self.imagem1: self.Click_Photo(self.imagem4, Parte, self.arq_Image_4))
        self.lbl_rosto4.pack()



        self.frm_rosto5 = tk.Frame(self.janela2, width=321, height=380, bg="#8B4513")
        self.frm_rosto5.grid(column=2, row=0)
        self.lbl_rosto5 = tk.Label(self.frm_rosto5, image=self.imagem5, width=341, height= 400)
        self.lbl_rosto5.bind("<Button-1>", lambda argumento_necesario = self.imagem1: self.Click_Photo(self.imagem5, Parte, self.arq_Image_5))
        self.lbl_rosto5.pack()



        self.frm_rosto6 = tk.Frame(self.janela2, width=321, height=380, bg="#FFFF00")
        self.frm_rosto6.grid(column=2, row=1)
        self.lbl_rosto6 = tk.Label(self.frm_rosto6, image=self.imagem6, width=341, height= 400)
        self.lbl_rosto6.bind("<Button-1>", lambda argumento_necesario = self.imagem1: self.Click_Photo(self.imagem6, Parte, self.arq_Image_6))
        self.lbl_rosto6.pack()


        self.lbl_rosto1.configure(image=self.imagem1)
        self.lbl_rosto1.image=self.imagem1
        self.lbl_rosto2.configure(image=self.imagem2)
        self.lbl_rosto2.image=self.imagem2
        self.lbl_rosto3.configure(image=self.imagem3)
        self.lbl_rosto3.image=self.imagem3
        self.lbl_rosto4.configure(image=self.imagem4)
        self.lbl_rosto4.image=self.imagem4
        self.lbl_rosto5.configure(image=self.imagem5)
        self.lbl_rosto5.image=self.imagem5
        self.lbl_rosto6.configure(image=self.imagem6)
        self.lbl_rosto6.image=self.imagem6

        Parte = Parte
        imagem = tk.PhotoImage(file="Images_Interface/duas-setas-para-a-esquerda.png")
        self.button_pass_esquerdo = tk.Button(self.janela2, image=imagem, command=lambda: [self.passa_esquerda(Parte)])
        self.button_pass_esquerdo.config(image=imagem)
        self.button_pass_esquerdo.imagem = imagem
        self.button_pass_esquerdo.grid(column=1, row=2, sticky=tk.W, padx=100)

        imagem = tk.PhotoImage(file="Images_Interface/avanco-rapido.png")
        self.button_pass_direito = tk.Button(self.janela2, image=imagem, command=lambda: [self.passa_direita(Parte)])
        self.button_pass_direito.config(image=imagem)
        self.button_pass_direito.imagem = imagem
        self.button_pass_direito.grid(column=1, row=2, sticky=tk.E, padx=100)

        #print(self.chave_nariz, self.chave_boca, self.chave_olhos)

 
    def passa_direita(self, Parte):
        if len(self.vetor_rostos) > self.termina:
            self.começa += 6
            self.termina += 6
            self.StartImgs(Parte)

            imagem1 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[0]}"))
            imagem2 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[1]}"))
            imagem3 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[2]}"))
            imagem4 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[3]}"))
            imagem5 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[4]}"))
            imagem6 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[5]}"))

            self.lbl_rosto1.configure(image=imagem1)
            self.lbl_rosto1.image=imagem1
            self.lbl_rosto2.configure(image=imagem2)
            self.lbl_rosto2.image=imagem2
            self.lbl_rosto3.configure(image=imagem3)
            self.lbl_rosto3.image=imagem3
            self.lbl_rosto4.configure(image=imagem4)
            self.lbl_rosto4.image=imagem4
            self.lbl_rosto5.configure(image=imagem5)
            self.lbl_rosto5.image=imagem5
            self.lbl_rosto6.configure(image=imagem6)
            self.lbl_rosto6.image=imagem6

    def passa_esquerda(self, Parte):
        if self.começa != 0:
            
            self.começa -= 6
            self.termina -= 6 
            self.StartImgs(Parte)
            
            imagem1 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[0]}"))
            imagem2 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[1]}"))
            imagem3 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[2]}"))
            imagem4 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[3]}"))
            imagem5 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[4]}"))
            imagem6 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[5]}"))

            self.lbl_rosto1.configure(image=imagem1)
            self.lbl_rosto1.image=imagem1
            self.lbl_rosto2.configure(image=imagem2)
            self.lbl_rosto2.image=imagem2
            self.lbl_rosto3.configure(image=imagem3)
            self.lbl_rosto3.image=imagem3
            self.lbl_rosto4.configure(image=imagem4)
            self.lbl_rosto4.image=imagem4
            self.lbl_rosto5.configure(image=imagem5)
            self.lbl_rosto5.image=imagem5
            self.lbl_rosto6.configure(image=imagem6)
            self.lbl_rosto6.image=imagem6


    def Click_Photo(self, event, Parte, arq):
            if Parte == "Rosto":
                self.image_label2.configure(image=event)
                self.image_label2.image=event
                self.janela2.destroy()

                self.Rosto_salva = f"{arq}"
                #print(arq)
                
            else:
                # Abrir imagem frontal
                img_front = arq
                
                # Abrir imagem de fundo
                img_back = self.Rosto_salva 

                frontImage = Image.open(img_front)
                frontImage = frontImage.resize((self.width, self.height))
                try:
                    img_back = Image.open(img_back)
                except:
                    pass
                background = img_back.resize((self.width, self.height))

                # Converter imagem para RGBA
                frontImage = frontImage.convert("RGBA")
                
                # Converter imagem para RGBA
                background = background.convert("RGBA")
                
                # Calcula a largura para estar no centro
                width = (background.width - frontImage.width) // 2
                
                # Calcula a altura para estar no centro
                height = (background.height - frontImage.height) // 2
                
                # Cole o frontImage em (largura, altura)
                background.paste(frontImage, (width, height), frontImage)

                imagem = ImageTk.PhotoImage(background)

                self.Rosto_salva = background

                self.image_label2.configure(image=imagem)
                self.image_label2.image=imagem
                self.janela2.destroy()


    def gerar_miniatura(self):
        for count_photo_baixo in range(1, 5):
            print(count_photo_baixo)
            if count_photo_baixo == 1 and self.baixo1 == False:
                try:
                    self.Rosto_salva = Image.open(self.Rosto_salva)
                except:
                    pass
                img_resized = self.Rosto_salva.resize((110, 130))
                # img_resized.save("IMAGENS-M/Lula.png")
                # img_resized.show()
                Imagem = ImageTk.PhotoImage(img_resized)
                self.Miniatura_01.configure(image=Imagem)
                self.Miniatura_01.image=Imagem
                self.baixo1 = True
                break

            elif count_photo_baixo == 2 and self.baixo2 == False:
                try:
                    self.Rosto_salva = Image.open(self.Rosto_salva)
                except:
                    pass
                img_resized = self.Rosto_salva.resize((110, 130))
                Imagem = ImageTk.PhotoImage(img_resized)
                self.Miniatura_02.configure(image=Imagem)
                self.Miniatura_02.image=Imagem
                self.baixo2 = True
                break

            elif count_photo_baixo == 3 and self.baixo3 == False:
                try:
                    self.Rosto_salva = Image.open(self.Rosto_salva)
                except:
                    pass
                img_resized = self.Rosto_salva.resize((110, 130))
                Imagem = ImageTk.PhotoImage(img_resized)
                self.Miniatura_03.configure(image=Imagem)
                self.Miniatura_03.image=Imagem
                self.baixo3 = True
                break
                
            elif count_photo_baixo == 4 and self.baixo4 == False:
                try:
                    self.Rosto_salva = Image.open(self.Rosto_salva)
                except:
                    pass
                img_resized = self.Rosto_salva.resize((110, 130))
                Imagem = ImageTk.PhotoImage(img_resized)
                self.Miniatura_04.configure(image=Imagem)
                self.Miniatura_04.image=Imagem
                self.baixo4 = True
                
    
    def excluir_miniaturas(self, escolha):
        if escolha == 1:
            self.Miniatura_01.configure(image=self.image_miniatura)
            self.Miniatura_01.image=self.image_miniatura
            self.baixo1 = False
        elif escolha == 2:
            self.Miniatura_02.configure(image=self.image_miniatura)
            self.Miniatura_02.image=self.image_miniatura
            self.baixo2 = False
        elif escolha == 3:
            self.Miniatura_03.configure(image=self.image_miniatura)
            self.Miniatura_03.image=self.image_miniatura
            self.baixo3 = False
        else:
            self.Miniatura_04.configure(image=self.image_miniatura)
            self.Miniatura_04.image=self.image_miniatura
            self.baixo4 = False



    def Salvar(self):
        print(self.Rosto_salva)


janela = tk.Tk()
Interface(janela)
janela.mainloop()

