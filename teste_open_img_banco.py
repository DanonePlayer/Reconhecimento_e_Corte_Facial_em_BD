import BD as bd

query = ("SELECT dados FROM imagens WHERE id=1")

dados = bd.consultar(query)


import cv2
import numpy as np

if dados:
    dados_binarios = dados[0][0]
    imagem = cv2.imdecode(np.frombuffer(dados_binarios, np.uint8), cv2.IMREAD_COLOR)

    # Agora 'imagem' contém a imagem recuperada

    cv2.imshow("Imagem", imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()