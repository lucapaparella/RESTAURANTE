import mysql.connector
import os
os.system("cls")
db_configuracao = {
    "host" : "localhost",
    "user" : "root",
    "password" : "root",
    "database" : "restaurante"
}
try:
    conexao = mysql.connector.connect(**db_configuracao)
    cursor = conexao.cursor()
    print("""
    █████████████████████████████████████████████████████████
    █▄─▀█▀─▄██▀▄─██▄─▀█▀─▄█▄─▀█▀─▄██▀▄─████▄─▀█▀─▄█▄─▄██▀▄─██
    ██─█▄█─███─▀─███─█▄█─███─█▄█─███─▀─█████─█▄█─███─███─▀─██
    ▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀""")


    print("\n")
    print("*"*25)
    print("1 - Adcionar Prato")
    print("2 - Atualizar Prato")
    print("3 - Apagar Prato")
    print("4 - Sair")
    print("*"*25)


    while True:
        while True:
            opcao = int(input("Escolha uma Opção:"))
            if opcao<1 or opcao>4:
                print("Opção Invalida...tente novamente!")
            else:
                break
        match opcao:
            case 1:
                nome = input("Qual o nome do prato? ")
                ingredientes = input("Quai os ingredientes? ")
                preco = float(input("Qual o preço do prato? "))
                query = f"insert into pratos(nome,ingredientes,preco) values ('{nome}','{ingredientes}',{preco})"
                cursor.execute(query)
                conexao.commit()
            case 2:
                query = "select * from pratos"
                cursor.execute(query)
                pratos = cursor.fetchall()
                conexao.commit()
                # print(pratos)
                for prato in pratos:
                    print(f"ID: {prato[0]} | Nome: {prato[1]} | Ing: {prato[2]} | Preço: {prato[3]}")
            case 3:
                pass
            case 4:
                break
    print("Programa encerrado com Sucesso!")
except mysql.connector.Error as erro:
    print(f"Banco de Dado com erro: {erro}")