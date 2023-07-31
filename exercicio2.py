#Escreva um programa que crie uma tupla com os meses do ano. 
#Em seguida, peça ao usuário para digitar um número de 1 a 12 e retorne o mês correspondente.

def obter_numero_mes():
    numero_mes = int(input("Digite um número de 1 a 12: "))
    mes_correspondente = obter_mes_correspondente(numero_mes)
    print(f"O mês correspondente é: {mes_correspondente}")

def obter_mes_correspondente(numero):
    meses_do_ano = (
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    )

    if 1 <= numero <= 12:
        return meses_do_ano[numero - 1]
    else:
        return "Mês inválido. Digite um número de 1 a 12."
    
obter_numero_mes()
     

