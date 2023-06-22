# Importar o módulo Aspose.Words para Python
import aspose.words as aw

# carregue o arquivo PDF e converta para o formato Word DOCX
pdf = aw.Document("ADRIANO.pdf")
pdf.save("pdf.docx")

# carregue a versão DOCX do PDF
doc = aw.Document("pdf.docx")

# recuperar todas as formas
shapes = doc.get_child_nodes(aw.NodeType.SHAPE, True)
imageIndex = 0

# loop através de formas
for shape in shapes :
    shape = shape.as_shape()
    if (shape.has_image):

        # definir o nome do arquivo de imagem
        imageFileName = f"Image.ExportImages.{imageIndex}_{aw.FileFormatUtil.image_type_to_extension(shape.image_data.image_type)}"

        # salvar imagem
        shape.image_data.save(imageFileName)
        imageIndex += 1