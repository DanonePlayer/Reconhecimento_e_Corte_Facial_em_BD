#USA O rosto.png COMO EXEMPLO DE TESTE, ELE É MAIS COMO UMA BASE, É PARECIDO COM MUITAS DAS IMAGENS DA BASE QUE VAMOS USAR
import io
import os

import cv2
import numpy as np
from PIL import Image

import BD as bd


def reconhecimento_e_corte_Rosto(progressbar, valor):
    query = f"SELECT id From Pessoas"
    dados = bd.consultar(query)

    barra_carregamento_max = len(dados) * 4
    cont_barra_de_carregamento = 0

    query = f"SELECT Imagem From Pessoas"
    dados = bd.consultar(query)
    
    for imgi in dados:
        # print(imgi)

        query_nomes = f"SELECT Nome FROM Pessoas WHERE Imagem = ?"
        dados_nomes = bd.consultar(query_nomes, (imgi[0],))
        nome_img = dados_nomes[0][0]

        query_ids_nomes = f"SELECT id FROM Pessoas WHERE Imagem = ?"
        dados_ids_nomes = bd.consultar(query_ids_nomes, (imgi[0],))
        id_nome = dados_ids_nomes[0][0]

        query = f"SELECT id From Rosto Where pessoa_id = {id_nome}"
        dados_old = bd.consultar(query)
        # print(dados_old)

        cont_barra_de_carregamento +=1
        valor_mapeado = ((cont_barra_de_carregamento - 0) / (barra_carregamento_max - 0)) * (101 - 0)  # Mapeia para 0 a 100
        valor_mapeado += valor
        # print(valor_mapeado)
        progressbar["value"] = valor_mapeado
        progressbar.update() 

        if dados_old == []:

            classificador = cv2.CascadeClassifier(r"anexos/right_eye2.xml")
            img = cv2.imdecode(np.frombuffer(imgi[0], np.uint8), cv2.IMREAD_COLOR)
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
            objetos = classificador.detectMultiScale(imgGray, minSize=(120,120), scaleFactor=1.1, minNeighbors=10, maxSize=(950,220))
            try:
                olho_esquerdo = objetos[0]
                olho_direito = objetos[1]
                cont = 1
            except:
                # print(f"{imgi} + Precisa Redimensionar, olho")
                cont = 0
                # Define os pontos dos vértices
                pts_olhos = np.array([[159, 246], [159, 387], [524, 384], [524, 246]], np.int32)


            if cont == 1:
                pts_olhos = np.array( [[olho_direito[0], olho_direito[1]],  
                                [olho_direito[0], olho_direito[1]+olho_direito[3]], 
                                [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]+olho_esquerdo[3]], 
                                [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]]], np.int32)

                pontos = [[olho_direito[0], olho_direito[1]],  
                                [olho_direito[0], olho_direito[1]+olho_direito[3]], 
                                [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]+olho_esquerdo[3]], 
                                [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]]]
                # print(pontos)

                if pontos[0][0] > pontos[0][1]:
                    olho_esquerdo = objetos[1]
                    olho_direito = objetos[0]
                    pts_olhos = np.array( [[olho_direito[0], olho_direito[1]],  
                        [olho_direito[0], olho_direito[1]+olho_direito[3]], 
                        [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]+olho_esquerdo[3]], 
                        [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]]], np.int32)

                    pontos = [[olho_direito[0], olho_direito[1]],  
                        [olho_direito[0], olho_direito[1]+olho_direito[3]], 
                        [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]+olho_esquerdo[3]], 
                        [olho_esquerdo[0]+olho_esquerdo[2], olho_esquerdo[1]]]
                    
                    # print(pontos)



            classificador = cv2.CascadeClassifier(r"anexos/nose.xml")
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
            objetos = classificador.detectMultiScale(imgGray, minSize=(120,120), scaleFactor=1.6, maxSize=(950,220))
            try:
                Nariz = objetos[0]
                cont = 1
            except:
                # print(f"{imgi}, Precisa Redimensionar, nariz")
                cont = 0
                # Define os pontos dos vértices
                pts_nariz = np.array([[226, 221], [226, 498], [415, 498], [415, 221]], np.int32)

            if cont == 1:
                pts_nariz = np.array( [[Nariz[0], Nariz[1]-120],  
                                [Nariz[0], Nariz[1]+Nariz[3]], 
                                [Nariz[0]+Nariz[2], Nariz[1]+Nariz[3]], 
                                [Nariz[0]+Nariz[2], Nariz[1]-120]], np.int32)
                
                pontos = [[Nariz[0], Nariz[1]-120],  
                                [Nariz[0], Nariz[1]+Nariz[3]], 
                                [Nariz[0]+Nariz[2], Nariz[1]+Nariz[3]], 
                                [Nariz[0]+Nariz[2], Nariz[1]-120]]
                # print(pontos)





            classificador = cv2.CascadeClassifier(r"anexos/mouth.xml")
            objetos = classificador.detectMultiScale(imgGray, minSize=(90,90), scaleFactor=1.1, minNeighbors=190, maxSize=(950,220)) # ou maxSize
            try:
                boca = objetos[0]
                cont = 1
            except:
                cont = 0
                # Define os pontos dos vértices
                pts_boca = np.array([[185, 486], [185, 614], [479, 614], [479, 486]], np.int32)
                # Cria uma máscara com os pontos

            if cont == 1:

                # img = cv2.imread("hascas/rosto.png")
                pts_boca = np.array( [[boca[0]-40, boca[1]],  
                                [boca[0]-40, boca[1]+boca[3]], 
                                [(boca[0]+40)+boca[2], boca[1]+boca[3]],
                                [(boca[0]+40)+boca[2], boca[1]]], np.int32)
                
                pontos = [[boca[0]-40, boca[1]],  
                                [boca[0]-40, boca[1]+boca[3]], 
                                [(boca[0]+40)+boca[2], boca[1]+boca[3]],
                                [(boca[0]+40)+boca[2], boca[1]]]
                
                # print(pontos)


            mask = np.zeros_like(img)
            cv2.fillPoly(mask, [pts_olhos], (255, 255, 255))

            # Aplica a máscara na imagem original
            part_cortada = cv2.bitwise_and(img, cv2.bitwise_not(mask))

            mask = np.zeros_like(part_cortada)
            cv2.fillPoly(mask, [pts_nariz], (255, 255, 255))

            # Aplica a máscara na imagem original
            part_cortada = cv2.bitwise_and(part_cortada, cv2.bitwise_not(mask))

            mask = np.zeros_like(part_cortada)
            cv2.fillPoly(mask, [pts_boca], (255, 255, 255))

            # Aplica a máscara na imagem original
            part_cortada = cv2.bitwise_and(part_cortada, cv2.bitwise_not(mask))

            # Converta a imagem para o formato RGB para exibição com matplotlib
            part_cortada = cv2.cvtColor(part_cortada, cv2.COLOR_BGR2RGB)


            #aqui iremos transforma o redor da imagem em transparente
            # Crie uma imagem Pillow (PIL) a partir da imagem RGB
            img = Image.fromarray(part_cortada)
            #convertida para o modo RGBA que significa que ela terá canais vermelho, verde, azul e alfa (transparência).
            rgba = img.convert("RGBA")
            # Isso obtém os dados de pixel da imagem, que incluirão informações sobre a cor e transparência de cada pixel.
            datas = rgba.getdata()
            
            newData = []
            for item in datas:
                # encontrando a cor preta pelo seu valor RGB
                if item[0] == 0 and item[1] == 0 and item[2] == 0:  
                    # Se o pixel for preto, ele é substituído por um pixel totalmente transparente
                    #  (branco com alfa 0), indicando que ele será tornando transparente.
                    newData.append((255, 255, 255, 0))
                else:
                    # outras cores permanecem inalteradas
                    newData.append(item)  
            # Aqui, os novos dados de pixel são aplicados à imagem RGBA.
            rgba.putdata(newData)
            #A imagem editada é salva
            dados_imagem = io.BytesIO()
            rgba.save(dados_imagem, format='PNG')
            query = "INSERT INTO Rosto (Imagem, pessoa_id) VALUES (?, ?)"
            valores = (dados_imagem.getvalue(), id_nome)
            bd.inserir(query, valores)
            # rgba.save(f"Rosto-{genero}\{imgi}", "PNG")


            # plt.imshow(img)
            # plt.imshow(img_cortada)
            # plt.imshow(part_cortada)
            # plt.axis('off')
            # plt.show()

    progressbar.destroy()