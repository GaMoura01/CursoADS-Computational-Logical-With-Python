#Escreva um programa que crie um dicionário com o nome e 
#a idade de três pessoas. Em seguida, solicite ao usuário 
#um nome e exiba a idade correspondente.

def obter_nome_idade(): 
    cadastro = [
        {"nome": "Gabriella", "idade": 19},        
        {"nome": "Gabriele", "idade": 24},
        {"nome": "Isabella", "idade": 24}
    ]
    return cadastro

def consultar_nome_idade():
    cadastro = obter_nome_idade()
    consulta = input("Digite um nome para consulta de idade no dicionário: ")
    for pessoa in cadastro: 
        if pessoa ["nome"] == consulta: 
            return pessoa["idade"]
    
    return "Nome não encontrado. Digite um nome novamente."

def resultado():
    idade = consultar_nome_idade()
    print(f"A pessoa informada tem {idade} anos.")

resultado()

