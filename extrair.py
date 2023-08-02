import os
import unicodedata
from tkinter import messagebox

import aspose.words as aw
import PyPDF2
from pdf2docx import Converter


def Gerador_imagens():
    Pdfs = os.listdir("Pdfs")
    Docx = os.listdir("Docx")

    i = 0 
    if Pdfs == []:
        messagebox.showerror(title="Erro", message="Sem Arquivos no Pdf")
    else:

        for Pdf in Pdfs:

            Pdfs = os.listdir("Pdfs")
            Docx = os.listdir("Docx")
            if Docx == []:
                # print(Pdf)
                # convert pdf to docx
                cv = Converter(f"Pdfs/{Pdf}")
                Pdf = Pdf.translate(str.maketrans("", "", ".pdf"))
                cv.convert(f"Docx/{Pdf}.docx")      # all pages by default
                cv.close()
                Docx = os.listdir("Docx")
                a = Pdfs[i]
                b = Docx[i]
            
            else:
                try:
                    a = Pdfs[i]
                    b = Docx[i]
                except:
                    print("Erro")
                    print(i)

                


                retira = ".docx.pdf"
                pdf = a.translate(str.maketrans("", "", retira))
                doc = b.translate(str.maketrans("", "", retira))



                if doc != pdf:
                    # print(i)
                    print(doc)
                    print(pdf)
                    


                    # print(Pdf)
                    # convert pdf to docx
                    cv = Converter(f"Pdfs/{Pdf}")
                    cv.convert(f"Docx/{pdf}.docx")      # all pages by default
                    cv.close()

            i += 1

        # imageIndex = 0

        Docx = os.listdir("Docx")
        contador = 0

        for Docx_name in Docx:
            # print(Docx_name)
            # load the Word document

            doc = aw.Document(f"Docx/{Docx_name}")

            # retrieve all shapes
            shapes = doc.get_child_nodes(aw.NodeType.SHAPE, True)

            Pdf = Pdfs[contador]

            # Abre o arquivo pdf 
            # lembre-se que para o windows você deve usar essa barra -> / 
            # lembre-se também que você precisa colocar o caminho absoluto
            pdf_file = open(f"Pdfs/{Pdf}", 'rb')

            #Faz a leitura usando a biblioteca
            read_pdf = PyPDF2.PdfFileReader(pdf_file)

            # pega o numero de páginas
            number_of_pages = read_pdf.getNumPages()

            #lê a primeira página completa
            page = read_pdf.getPage(0)

            #extrai apenas o texto
            page_content = page.extractText()

            # faz a junção das linhas 
            parsed = ''.join(page_content)

            # print("Sem eliminar as quebras")
            # print(parsed)

            pagi = parsed.split()

            for palavras in pagi:
                if palavras == "MASCULINO":
                    # print(Docx_name)
                    cont = 0 
                    # loop through shapes
                    for shape in shapes :
                        shape = shape.as_shape()
                        if (shape.has_image) :
                            cont +=1

                            if cont == 2:

                                retira = ".docx.pdf"
                                Docx_name = Docx_name.translate(str.maketrans("", "", retira))

                                Docx_name = unicodedata.normalize("NFD", Docx_name)
                                Docx_name = Docx_name.encode("ascii", "ignore")
                                Docx_name = Docx_name.decode("utf-8")


                                # set image file's name
                                imageFileName = f"{Docx_name}{aw.FileFormatUtil.image_type_to_extension(shape.image_data.image_type)}"
                                # print(imageFileName)
                                # save image

                                shape.image_data.save(f"IMAGENS-M/{imageFileName}")
                                # imageIndex += 1
                elif palavras == "FEMININO":
                    cont = 0
                    # loop through shapes
                    for shape in shapes :
                        shape = shape.as_shape()
                        if (shape.has_image) :
                            cont +=1

                            if cont == 2:

                                retira = ".docx.pdf"
                                Docx_name = Docx_name.translate(str.maketrans("", "", retira))

                                Docx_name = unicodedata.normalize("NFD", Docx_name)
                                Docx_name = Docx_name.encode("ascii", "ignore")
                                Docx_name = Docx_name.decode("utf-8")


                                # set image file's name
                                imageFileName = f"{Docx_name}{aw.FileFormatUtil.image_type_to_extension(shape.image_data.image_type)}"
                                # print(imageFileName)
                                # save image

                                shape.image_data.save(f"IMAGENS-F/{imageFileName}")
                                # imageIndex += 1
            contador +=1