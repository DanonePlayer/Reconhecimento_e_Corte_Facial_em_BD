import io

from PIL import Image

import BD as bd

query = f"SELECT Imagem From Pessoas WHERE id = 1"
dados = bd.consultar(query)
print(dados[0][0])
# image1 = Image.open(io.BytesIO(dados[0][0]))