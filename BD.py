import os
import sqlite3
from sqlite3 import Error


def conexao_banco():
    dir = os.path.dirname(__file__)
    caminho = f"{dir}/banco_sistema_imagens.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
        return con
    except Error as error:
        print(error)
def inserir(insert, parametros=None):
    try:
        con = conexao_banco()
        cursor = con.cursor()
        if parametros:
            cursor.execute(insert, parametros)
        else:
            cursor.execute(insert)
        con.commit()
        con.close()
        print("Inserido com sucesso")
    except Error as error:
        print(error)

def atualizar(update, parametros=None):
    try:
        con = conexao_banco()
        cursor = con.cursor()
        if parametros:
            cursor.execute(update, parametros)
        else:
            cursor.execute(update)
        con.commit()
        con.close()
        print("Atualizado com sucesso")
    except Error as error:
        print(error)

def deletar(delete):
    try:
        con = conexao_banco()
        cursor = con.cursor()
        cursor.execute(delete)
        con.commit()
        con.close()
        print("Removido com sucesso")
    except Error as error:
        print(error)

def consultar(consultar, parametros=None):
    try:
        con = conexao_banco()
        cursor = con.cursor()
        if parametros:
            cursor.execute(consultar, parametros)
        else:
            cursor.execute(consultar)
        valores = cursor.fetchall()
        con.close()
        # print("consuta feita com sucesso")
        return valores
    except Error as error:
        print(error)

# Nome do banco de dados que você deseja verificar
nome_banco_dados = 'banco_sistema_imagens.db'

# Verifique se o arquivo do banco de dados existe
if os.path.exists(nome_banco_dados):
    try:
        # Tente abrir o banco de dados
        conn = sqlite3.connect(nome_banco_dados)
        conn.close()
        print(f"O banco de dados '{nome_banco_dados}' existe e é acessível.")
    except sqlite3.Error as e:
        print(f"O arquivo '{nome_banco_dados}' existe, mas houve um erro ao tentar acessá-lo: {e}")
else:
    print(f"O banco de dados '{nome_banco_dados}' não existe. A ser criado agora.")


    query = ('''CREATE TABLE IF NOT EXISTS Pessoas (id INTEGER PRIMARY KEY, Nome TEXT, Sexo VARCHAR, Imagem BLOB)''')
    inserir(query)

    query = ('''CREATE TABLE IF NOT EXISTS Rosto (id INTEGER PRIMARY KEY, Imagem BLOB, pessoa_id INTEGER, FOREIGN KEY (pessoa_id) REFERENCES Pessoas(id))''')
    inserir(query)

    query = ('''CREATE TABLE IF NOT EXISTS Olhos (id INTEGER PRIMARY KEY, Imagem BLOB, pessoa_id INTEGER, FOREIGN KEY (pessoa_id) REFERENCES Pessoas(id))''')
    inserir(query)

    query = ('''CREATE TABLE IF NOT EXISTS Nariz (id INTEGER PRIMARY KEY, Imagem BLOB, pessoa_id INTEGER, FOREIGN KEY (pessoa_id) REFERENCES Pessoas(id))''')
    inserir(query)

    query = ('''CREATE TABLE IF NOT EXISTS Boca (id INTEGER PRIMARY KEY, Imagem BLOB, pessoa_id INTEGER, FOREIGN KEY (pessoa_id) REFERENCES Pessoas(id))''')
    inserir(query)














# with open('IMAGENS-M\Teste-1.png', 'rb') as arquivo_imagem:
#     dados_imagem = arquivo_imagem.read()


# query = "INSERT INTO Pessoas (Nome, Sexo, Imagem) VALUES (?, ?, ?)"

# valores = ('Teste-1', "Masculino", dados_imagem)

# inserir(query, valores)





# query = "SELECT id From Pessoas Where Nome Like 'Teste-1'"

# dados = consultar(query)

# print(dados[0][0])





# query = "INSERT INTO Rosto (Imagem, pessoa_id) VALUES (?, ?)"


# valores = (dados_imagem, dados[0][0])

# inserirImg(query, valores)
