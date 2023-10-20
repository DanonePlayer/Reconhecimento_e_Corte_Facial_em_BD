import io

from PIL import Image

import BD as bd

vet = []
for id in range(1, 10):
    query = f"SELECT id From Rosto WHERE id = {id}"
    dados = bd.consultar(query)
    vet.append(dados[0])
print(vet[0][0])
# image1 = Image.open(io.BytesIO(dados[0][0]))