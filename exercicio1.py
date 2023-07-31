#1. Crie um programa que solicite ao usuário uma lista de 
#números inteiros e retorne a soma de todos os elementos da lista.

#Para obtermos a lista de números inteiros usamos esta função,
#a variavel números solicita que o usúario digite uma lista de números
#separados por espaço e é lida como uma string. O código 
#lista = [int(numero) for numero in numeros.split()] usa uma list comprehension
#para criar uma lista de números inteiros. A string é dividida em substrings usando
#o método split() que é um separador. Cada substring é convertida em um número
#inteiro (int(numero)) e os mesmos são armazenados la 'lista'.

def obter_lista_numeros():

    numeros= input("Digite uma lista de números separados por espaço:")
    lista= [int(numero) for numero in numeros.split()]
    return lista

#A função def calcular soma recebe uma lista de núemros inteiros e calcula
#a soma de todos os elementos da lista usando a função 'sum()'do Python.

def calcular_soma(lista):
    soma = sum(lista)
    return soma

#A função def resultado chama as funçoes obter_lista_numero() e calcular_soma()
#para obter a ista de números do usuário e calcular a soma dos elementos. O print
#exibe o resultado no terminal.

def resultado():
    lista_numeros = obter_lista_numeros()
    soma = calcular_soma(lista_numeros)
    print(f"A soma dos números da lista é: {soma}")

#A função resultado() é chamada, iniciando a execução do programa.

resultado()
