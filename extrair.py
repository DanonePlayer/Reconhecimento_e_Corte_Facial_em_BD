import io
import os
import unicodedata
from tkinter import messagebox

import aspose.words as aw
import PyPDF2
from pdf2docx import Converter

import BD as bd


def Gerador_imagens(progressbar):
    #pegando as pastas destinos e listando os arquivos dentro delas
    Pdfs = os.listdir("Pdfs")
    Docx = os.listdir("Docx")

    contador_arqs = 0 

    #verifica se há arquivos dentro da pasta PDF
    if Pdfs == []:
        messagebox.showerror(title="Erro", message="Sem Arquivos no Pdf")

    else:
        #PEGANDO ARQUIVO POR ARQUIVO DE DENTRO DE PDFS
        for Pdf in Pdfs:
            #Sempre atualizando a listagem das pastas
            Pdfs = os.listdir("Pdfs")
            Docx = os.listdir("Docx")
            #verifica se há arquivos dentro da pasta WORD
            if Docx == []:
                # print(Pdf)
                # converte pdf para docx
                cv = Converter(f"Pdfs/{Pdf}")
                #tira das pastas de dentro de pdf o tipo do arquivo, no caso o ".pdf"
                Pdf = Pdf.translate(str.maketrans("", "", ".pdf"))
                #Onde irei guardar e qual a sua extensão
                cv.convert(f"Docx/{Pdf}.docx")
                cv.close()
                # Novamente atualizando a listagem da pasta DOCX
                Docx = os.listdir("Docx")
                #guarda os arquivos que estão sendo processados no momento e verfica se as duas pastas tem a mesma quantidade de arquivos
                a = Pdfs[contador_arqs]
                b = Docx[contador_arqs]
            else:
                try:
                    # verificar se a quantidade de contador_arqs em pdfs é igual a de docxs
                    a = Pdfs[contador_arqs]
                    b = Docx[contador_arqs]
                except:
                    pass
                    #caso não for apenas printa para não parar o codigo
                    # print("Erro, há uma pasta a mais em pdf")
                    # print(contador_arqs)

                

                # print(a,b)
                retira = ".docx.pdf"
                pdf = a.translate(str.maketrans("", "", retira))
                doc = b.translate(str.maketrans("", "", retira))


                
                if doc != pdf:
                    # print(contador_arqs)
                    # print(doc)
                    # print(pdf)
                    


                    # print(Pdf)
                    cv = Converter(f"Pdfs/{Pdf}")
                    cv.convert(f"Docx/{pdf}.docx") 
                    cv.close()

            contador_arqs += 1

        #converter os docx em img e pega palavras dentro de PDF
        Docx = os.listdir("Docx")
        contador = 0

        barra_carregamento_max = len(Docx)
        for Docx_name in Docx:
            valor_mapeado = ((contador - 0) / (barra_carregamento_max - 0)) * (101 - 0)  # Mapeia para 0 a 100
            # print(valor_mapeado)
            progressbar["value"] = valor_mapeado
            progressbar.update() 
            # print(Docx_name)
            
            # carrega o documento Word
            doc = aw.Document(f"Docx/{Docx_name}")

            
            # buscando todas as formas gráficas no documento.
            shapes = doc.get_child_nodes(aw.NodeType.SHAPE, True)
            # print(shapes)
            Pdf = Pdfs[contador]

            # Abre o arquivo pdf 
            # lembre-se que para o windows você deve usar essa barra -> / 
            # lembre-se também que você precisa colocar o caminho absoluto
            pdf_file = open(f"Pdfs/{Pdf}", 'rb')

            #Faz a leitura usando a biblioteca
            read_pdf = PyPDF2.PdfReader(pdf_file)

            # pega o numero de páginas
            number_of_pages = len(read_pdf.pages)

            #lê a primeira página completa
            page = read_pdf.pages[0]

            #extrai apenas o texto
            page_content = page.extract_text()

            # faz a junção das linhas
            parsed = ''.join(page_content)

            # print("Sem eliminar as quebras")
            # print(parsed)

            #cria uma lista das palavras
            pagi = parsed.split()

            for palavras in pagi:
                # print(palavras)
                if palavras == "MASCULINO":
                    # print(Docx_name)
                    cont = 0 
                    # Percorre todas as formas gráficas no documento.
                    for shape in shapes :
                        #transformando o objeto em uma representação mais formal ou específica de uma forma gráfica.
                        shape = shape.as_shape()
                        #Verifica se é uma imagem
                        if (shape.has_image) :
                            cont +=1
                            #pega a imagem 2
                            if cont == 1:

                                # esse trecho de código estar trabalhando para limpar e normalizar o nome de um arquivo,
                                # removendo acentos, caracteres especiais e caracteres não ASCII,
                                # a fim de obter um nome de arquivo mais padronizado e
                                # compatível com sistemas que não suportam esses caracteres. 
                                retira = ".docx.pdf"
                                Docx_name = Docx_name.translate(str.maketrans("", "", retira))

                                Docx_name = unicodedata.normalize("NFD", Docx_name)
                                Docx_name = Docx_name.encode("ascii", "ignore")
                                Docx_name = Docx_name.decode("utf-8")


                                # definir o nome do arquivo de imagem
                                # recebe um tipo de imagem (como JPEG, PNG etc.) como argumento e retorna a extensão de arquivo
                                # associada a esse tipo de imagem.
                                imageFileName = f"{Docx_name}{aw.FileFormatUtil.image_type_to_extension(shape.image_data.image_type)}"
                                # print(imageFileName)

                                # save image
                                shape.image_data.save(f"IMAGENS-M/{imageFileName}")

                                # Converte os dados da imagem em um formato que possa ser armazenado no banco de dados
                                dados_imagem = io.BytesIO()
                                shape.image_data.save(dados_imagem)

                                query = "INSERT INTO Pessoas (Nome, Sexo, Imagem) VALUES (?, ?, ?)"

                                valores = (imageFileName, "Masculino", dados_imagem.getvalue())

                                bd.inserirImg(query, valores)

                elif palavras == "FEMININO":
                    cont = 0
                    # loop through shapes
                    for shape in shapes :
                        shape = shape.as_shape()
                        if (shape.has_image) :
                            cont +=1

                            if cont == 1:

                                retira = ".docx.pdf"
                                Docx_name = Docx_name.translate(str.maketrans("", "", retira))

                                Docx_name = unicodedata.normalize("NFD", Docx_name)
                                Docx_name = Docx_name.encode("ascii", "ignore")
                                Docx_name = Docx_name.decode("utf-8")


                                imageFileName = f"{Docx_name}{aw.FileFormatUtil.image_type_to_extension(shape.image_data.image_type)}"
                                # print(imageFileName)

                                shape.image_data.save(f"IMAGENS-F/{imageFileName}")

                                dados_imagem = io.BytesIO()
                                shape.image_data.save(dados_imagem)

                                query = "INSERT INTO Pessoas (Nome, Sexo, Imagem) VALUES (?, ?, ?)"

                                valores = (imageFileName, "Feminino", dados_imagem.getvalue())

                                bd.inserirImg(query, valores)
            contador +=1
    progressbar.destroy()