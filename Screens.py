##from PIL import Image, ImageTk
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
        self.frm_center_main.pack(fill=tk.BOTH, expand=True)

        self.label_programa = tk.Label(self.frm_center_main, text="PROGRAMA DE RECORTE E RECONHECIMENTO", font=('Roboto', 20), bg='#303030',fg='white')
        self.label_programa.pack(pady=(50, 0))

        self.label_versao = tk.Label(self.frm_center_main, text="Versão ALFA", font=('Roboto', 16), bg='#303030', fg='white')
        self.label_versao.pack(pady=(0, 40))

        self.image_label1 = tk.Label(self.frm_center_main, bg='white', width=41, height= 30)
        self.image_label1.pack(padx=50, pady=(10,70),side=tk.LEFT,fill=tk.BOTH)

        self.image_label2 = tk.Label(self.frm_center_main, bg='white',width=41, height= 30)
        self.image_label2.pack(padx=50, pady=(10,70),side=tk.RIGHT,fill=tk.BOTH)

        self.imagem_d = (f"Rosto_Inicial.png")
        self.imagem_d_lbl = ImageTk.PhotoImage(Image.open(self.imagem_d))

        self.label_imagem_original = tk.Label(self.frm_center_main, image=self.imagem_d_lbl, text="IMAGEM ORIGINAL", bg='#303030', fg='white',width=51, height= 40)
        self.label_imagem_original.pack(in_=self.image_label1, pady=(0, 5))

        self.label_imagem_original.configure(image=self.imagem_d_lbl)
        self.label_imagem_original.image=self.imagem_d_lbl

        self.btn = tk.Button(self.image_label1, text='Miniatura',borderwidth=0,font=('Arial',14, 'bold'), fg='#fff',bg='#5B5A5A')
        self.btn.pack(side=tk.BOTTOM,expand=True,pady=(0, 5))

        self.imagem_e = ImageTk.PhotoImage(Image.open(f"Rosto_Inicial.png"))

        self.label_recorde = tk.Label(self.frm_center_main, image=self.imagem_e, text="RECORTE", bg='#303030', fg='white',width=51, height= 40)
        self.label_recorde.pack(in_=self.image_label2, pady=(0, 5))

        self.label_recorde.configure(image=self.imagem_e)
        self.label_recorde.image=self.imagem_e

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

        self.imagem1 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[0]}"))
        self.arq_Image_1 = (f"{Parte}-M/{self.vetor_rostos[0]}")
        self.imagem2 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[1]}"))
        self.arq_Image_2 = (f"{Parte}-M/{self.vetor_rostos[1]}")
        self.imagem3 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[2]}"))
        self.arq_Image_3 = (f"{Parte}-M/{self.vetor_rostos[2]}")
        self.imagem4 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[3]}"))
        self.arq_Image_4 = (f"{Parte}-M/{self.vetor_rostos[3]}")
        self.imagem5 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[4]}"))
        self.arq_Image_5 = (f"{Parte}-M/{self.vetor_rostos[4]}")
        self.imagem6 = ImageTk.PhotoImage(Image.open(f"{Parte}-M/{self.vetor_rostos[5]}"))
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
        imagem = tk.PhotoImage(file="duas-setas-para-a-esquerda.png")
        self.button_pass_esquerdo = tk.Button(self.janela2, image=imagem, command=lambda: [self.passa_esquerda(Parte)])
        self.button_pass_esquerdo.config(image=imagem)
        self.button_pass_esquerdo.imagem = imagem
        self.button_pass_esquerdo.grid(column=1, row=2, sticky=tk.W, padx=100)

        imagem = tk.PhotoImage(file="avanco-rapido.png")
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
                self.label_imagem_original.configure(image=event)
                self.label_imagem_original.image=event
                self.janela2.destroy()
                self.imagem_d = arq

                self.Rosto_salva = f"{arq}"
                #print(arq)

    def gerar_miniatura(self):
        for count_photo_baixo in range(1, 5):
            print(count_photo_baixo)
            if count_photo_baixo == 1 and self.baixo1 == False:

                img = Image.open(self.Rosto_salva)
                img_resized = img.resize((190, 249))
                # img_resized.save("IMAGENS-M/Lula.png")
                # img_resized.show()
                Imagem = ImageTk.PhotoImage(img_resized)
                self.lbl_baixo1.configure(image=Imagem)
                self.lbl_baixo1.image=Imagem
                self.baixo1 = True
                break

            elif count_photo_baixo == 2 and self.baixo2 == False:

                img = Image.open(self.Rosto_salva)
                img_resized = img.resize((190, 249))
                Imagem = ImageTk.PhotoImage(img_resized)
                self.lbl_baixo2.configure(image=Imagem)
                self.lbl_baixo2.image=Imagem
                self.baixo2 = True
                break

            elif count_photo_baixo == 3 and self.baixo3 == False:

                img = Image.open(self.Rosto_salva)
                img_resized = img.resize((190, 249))
                Imagem = ImageTk.PhotoImage(img_resized)
                self.lbl_baixo3.configure(image=Imagem)
                self.lbl_baixo3.image=Imagem
                self.baixo3 = True
                break
                
            elif count_photo_baixo == 4 and self.baixo4 == False:
                img = Image.open(self.Rosto_salva)
                img_resized = img.resize((190, 249))
                Imagem = ImageTk.PhotoImage(img_resized)
                self.lbl_baixo4.configure(image=Imagem)
                self.lbl_baixo4.image=Imagem
                self.baixo4 = True
                
    
    def excluir_miniaturas(self, escolha):
        if escolha == 1:
            self.lbl_baixo1.configure(image=self.padr_baixo_arq)
            self.lbl_baixo1.image=self.padr_baixo_arq
            self.baixo1 = False
        elif escolha == 2:
            self.lbl_baixo2.configure(image=self.padr_baixo_arq)
            self.lbl_baixo2.image=self.padr_baixo_arq
            self.baixo2 = False
        elif escolha == 3:
            self.lbl_baixo3.configure(image=self.padr_baixo_arq)
            self.lbl_baixo3.image=self.padr_baixo_arq
            self.baixo3 = False
        else:
            self.lbl_baixo4.configure(image=self.padr_baixo_arq)
            self.lbl_baixo4.image=self.padr_baixo_arq
            self.baixo4 = False



    def Salvar(self):
        print(self.Rosto_salva)


janela = tk.Tk()
Interface(janela)
janela.mainloop()

