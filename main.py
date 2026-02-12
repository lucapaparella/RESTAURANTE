import mysql.connector
import os
os.system("cls")
db_configuracao = {
    "host" : "paparella.com.br",
    "user" : "paparell_aluno_3",
    "password" : "@Senai2025",
    "database" : "paparell_restaurante"
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
    print("4 - listar Pratos")
    print("5 - Cadastrar funcionario")
    print("6 - Listar funcionario")
    print("7 - Apagar Funcionario")
    print("8 - Sair")
    print("*"*25)


    while True:
        while True:
            opcao = int(input("Escolha uma Opção: "))
            if opcao<1 or opcao>8:
                print("Opção Invalida...tente novamente!")
            else:
                break
        match opcao:
            case 1:
                nome = input("Qual o nome do prato? ")
                ingredientes = input("Quais os ingredientes? ")
                preco = float(input("Qual o preço do prato? "))
                query = f"insert into pratos(nome,ingredientes,preco) values (%s,%s,%s)"
                cursor.execute(query,(nome,ingredientes,preco))
                if conexao.commit()== None:
                    print("Prato gravado com Sucesso!!!")
            case 2:
                query = "select * from pratos"
                cursor.execute(query)
                pratos = cursor.fetchall()
                conexao.commit()
                # print(pratos)
                for prato in pratos:
                    print(f"ID: {prato[0]} | Nome: {prato[1].center(20)} | Ing: {prato[2].center(20)} | Preço: R${prato[3]}")
                id = int(input("Digite o Numero do prato: "))
                nome = input("Digite novamente o nome do prato: ")
                ingredientes = input("Digite novamente os ingredientes: ")
                preco = float(input("Digite novamente o preço do prato: "))
                query = f"update pratos set nome=%s, ingredientes =%s,preco=%s where id=%s"
                cursor.execute(query,(nome,ingredientes,preco,id))
                
                if conexao.commit()== None:
                    print("Prato Atualizado com Sucesso!!!")

            case 3:
                query = "select * from pratos"
                cursor.execute(query)
                pratos = cursor.fetchall()
                conexao.commit()
                # print(pratos)
                for prato in pratos:
                    print(f"ID: {prato[0]} | Nome: {prato[1].center(20)} | Ing: {prato[2].center(20)} | Preço: {prato[3]}")
                id = int(input("Qual o ID que gostar de apagar? "))
                query = "Delete from pratos where id= %s"
                cursor.execute(query,(id,)) # importante a virgola com 1 dado somente...
                if conexao.commit()== None:
                    print("Prato Apagado com Sucesso!!!")
            case 4:
                query = "select * from pratos"
                cursor.execute(query)
                pratos = cursor.fetchall()
                conexao.commit()
                for prato in pratos:
                    print(f"ID: {prato[0]} | Nome: {prato[1].center(20)} | Ing: {prato[2].center(20)} | Preço: R${prato[3]}")
            case 5:
                nome = input("Qual o seu Nome? ")
                sobrenome = input("Qual o seu Sobrenome? ")
                cidade = input("Qual a sua Cidade? ")
                query = "insert into funcionarios(nome,sobrenome,cidade) values (%s,%s,%s)"
                cursor.execute(query,(nome,sobrenome,cidade))
                if conexao.commit()== None:
                    print("Funcionario gravado com Sucesso!!!")
            case 6:
                pass
            case 7:
                pass   
            case 8:
                break
    print("Programa encerrado com Sucesso!")
except mysql.connector.Error as erro:
    print(f"Banco de Dado com erro: {erro}")