import os
import tkinter as tk
from tkinter import SUNKEN, PhotoImage

from PIL import Image, ImageTk

# import recorte
# import extrair


class Interface_rostos:
    def __init__(self, master):
        self.janelaprincipal = master
        self.janelaprincipal.title("Rawn")
        self.janelaprincipal.configure(bg='#8F8B8B')
        self.janelaprincipal.geometry("1366x920")
        self.janelaprincipal.resizable(width=False, height=False)



        self.espaço = tk.Label(self.janelaprincipal, bg='#8F8B8B')
        self.espaço.grid(column=0, row=0, padx=60)

        self.espaço1 = tk.Label(self.janelaprincipal, width=60, height=10, bg='#8F8B8B' )
        self.espaço1.grid(column=1, row=0)

        self.frm_direito = tk.Frame(self.janelaprincipal, width=341, height=400, bg='#8F8B8B')
        self.frm_direito.grid(column=2, row=1, padx=40)

        self.imagem_d = (f"Rosto_Inicial.png")
        self.imagem_d_lbl = ImageTk.PhotoImage(Image.open(self.imagem_d))
        self.lbl_d = tk.Label(self.frm_direito, image=self.imagem_d_lbl, width=341, height= 400)
        self.lbl_d.pack()

        self.lbl_d.configure(image=self.imagem_d_lbl)
        self.lbl_d.image=self.imagem_d_lbl

        self.button_gerar_miniatura = tk.Button(self.janelaprincipal, text="Gerar Miniatura", command=self.gerar_miniatura)
        self.button_gerar_miniatura.place(x=850, y=570)

        self.frm_esquerdo = tk.Frame(self.janelaprincipal, width=341, height=400, bg='#8F8B8B')
        self.frm_esquerdo.grid(column=1, row=1)

        self.imagem_e_lbl = ImageTk.PhotoImage(Image.open(f"Rosto_Inicial.png"))
        self.lbl_e = tk.Label(self.frm_esquerdo, image=self.imagem_e_lbl, width=341, height=400)
        self.lbl_e.pack()

        self.lbl_e.configure(image=self.imagem_e_lbl)
        self.lbl_e.image=self.imagem_e_lbl


        self.frm_baixo = tk.Frame(self.janelaprincipal, width=400, height=400, bg='#8F8B8B')
        self.frm_baixo.grid(column=1, row=2, columnspan=2)

        self.padr_baixo = ("Lula.png")
        self.padr_baixo_arq = ImageTk.PhotoImage(Image.open(self.padr_baixo))

        self.count_photo_baixo = 1

        self.lbl_baixo1 = tk.Label(self.frm_baixo, image=self.padr_baixo_arq)
        self.lbl_baixo1.pack(side=tk.LEFT, padx=40)
        self.lbl_baixo2 = tk.Label(self.frm_baixo, image=self.padr_baixo_arq)
        self.lbl_baixo2.pack(side=tk.LEFT)
        self.lbl_baixo3 = tk.Label(self.frm_baixo, image=self.padr_baixo_arq)
        self.lbl_baixo3.pack(side=tk.LEFT, padx=40)
        self.lbl_baixo4 = tk.Label(self.frm_baixo, image=self.padr_baixo_arq)
        self.lbl_baixo4.pack(side=tk.LEFT)

        self.lbl_baixo1.configure(image=self.padr_baixo_arq)
        self.lbl_baixo1.image=self.padr_baixo_arq
        self.lbl_baixo2.configure(image=self.padr_baixo_arq)
        self.lbl_baixo2.image=self.padr_baixo_arq
        self.lbl_baixo3.configure(image=self.padr_baixo_arq)
        self.lbl_baixo3.image=self.padr_baixo_arq
        self.lbl_baixo4.configure(image=self.padr_baixo_arq)
        self.lbl_baixo4.image=self.padr_baixo_arq

        self.button_gerar_img_and_word = tk.Button(self.espaço1, text="Gerar Img and Word", command="self.Gerador")
        self.button_gerar_img_and_word.place(x=1, y=50)

        self.button_gerar_corte = tk.Button(self.espaço1, text="Gerar Cortes", command="self.recortes")
        self.button_gerar_corte.place(x=220, y=50  )

        self.frm_seleção = tk.Frame(self.janelaprincipal, width=90, height=400, bg='#8F8B8B')
        self.frm_seleção.grid(column=3, row=1, padx=60)

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


        self.button_Rosto = tk.Button(self.frm_seleção, text="Rosto" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0, command=self.Rosto)
        self.button_Rosto.place(x=1, y=202)


        self.button_Olhos = tk.Button(self.frm_seleção, text="Olhos" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0, command=self.Olhos)
        self.button_Olhos.place(x=1, y=233)


        self.button_Nariz = tk.Button(self.frm_seleção, text="Nariz" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0, command=self.Nariz)
        self.button_Nariz.place(x=1, y=264)


        self.button_Boca = tk.Button(self.frm_seleção, text="Boca" ,width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0, command=self.Boca)
        self.button_Boca.place(x=1, y=295)



        self.frm_salvamento = tk.Frame(self.janelaprincipal, width=90, height=400, bg='#8F8B8B')
        self.frm_salvamento.grid(column=3, row=2, padx=10)



        self.button_login = tk.Button(self.frm_salvamento, text="Exportar", width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0)
        self.button_login.place(x=1, y=1)


        self.button_login = tk.Button(self.frm_salvamento, text="Salvar", width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0, command="self.Salvar")
        self.button_login.place(x=1, y=31)


        self.button_login = tk.Button(self.frm_salvamento, text="Carregar", width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0)
        self.button_login.place(x=1, y=61)


        self.button_login = tk.Button(self.frm_salvamento, text="Novo", width=10, overrelief=tk.RIDGE, bd=3, activebackground="blue", underline=0)
        self.button_login.place(x=1, y=91)

        self.começa = 0
        self.termina = 6


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
        self.janela2.resizable(width=False, height=False )


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
                self.lbl_d.configure(image=event)
                self.lbl_d.image=event
                self.janela2.destroy()
                self.imagem_d = arq

                self.Rosto_salva = f"{arq}"
                #print(arq)

    def gerar_miniatura(self):
        
        if self.count_photo_baixo == 1:

            img = Image.open(self.Rosto_salva)
            img_resized = img.resize((190, 249))
            # img_resized.save("IMAGENS-M/Lula.png")
            # img_resized.show()
            Imagem = ImageTk.PhotoImage(img_resized)
            self.lbl_baixo1.configure(image=Imagem)
            self.lbl_baixo1.image=Imagem

            self.count_photo_baixo +=1

        elif self.count_photo_baixo == 2:

            img = Image.open(self.Rosto_salva)
            img_resized = img.resize((190, 249))
            Imagem = ImageTk.PhotoImage(img_resized)
            self.lbl_baixo2.configure(image=Imagem)
            self.lbl_baixo2.image=Imagem

            self.count_photo_baixo +=1

        elif self.count_photo_baixo == 3:

            img = Image.open(self.Rosto_salva)
            img_resized = img.resize((190, 249))
            Imagem = ImageTk.PhotoImage(img_resized)
            self.lbl_baixo3.configure(image=Imagem)
            self.lbl_baixo3.image=Imagem

            self.count_photo_baixo +=1
             
        else:
            img = Image.open(self.Rosto_salva)
            img_resized = img.resize((190, 249))
            Imagem = ImageTk.PhotoImage(img_resized)
            self.lbl_baixo4.configure(image=Imagem)
            self.lbl_baixo4.image=Imagem

    def Salvar(self):
        print(self.Rosto_salva)

        
janela = tk.Tk()
Interface_rostos(janela)
janela.mainloop()
