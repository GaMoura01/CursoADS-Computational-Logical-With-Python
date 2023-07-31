#Crie um programa que exiba um menu com 5 opções para o usuário. 
#A última opção deve ser "0" para sair do programa. 
#Cada opção do menu deve exibir informações relevantes, 
#sem interação do usuário.

def exibir_menu():
    print("----- Menu -----") 
    print("1. Informações sobre este programa. ")
    print("2. Informações sobre o desenvolvedor. ")
    print("3. Informações sobre a versão deste programa. ")
    print("4. Suporte. ")
    print("0. Sair do programa. ")

def exibir_informacoes_programa():
    print("Este programa para demonstrar o uso de um menu. ")
    print("Ele foi desenvolvido em linguagem Python. ")

def exibir_informacoes_desenvolvedor():
    print("Este programa foi criado por Gabriella Moura")
    print("Criado com finalidades educacionais. ")

def exibir_informacoes_versao():
    print("Este programa se encontra na versão 1.0. ")

def exibir_informacoes_suporte():
    print("Entrar em contato no número: 119999.9997 ou abrir um chamado em nosso site: dev@ga.com.br. ")

while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        exibir_informacoes_programa()
    elif opcao == "2":
        exibir_informacoes_desenvolvedor()
    elif opcao == "3":
        exibir_informacoes_versao()
    elif opcao == "4":
        exibir_informacoes_suporte()
    elif opcao == "0":
        print("Saindo do programa. Até logo! ")
        break
    else:
        print("Opção inválida. Digite uma opção válida. ")


