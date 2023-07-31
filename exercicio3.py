#Crie um programa que solicite ao usuário duas listas de 
#números inteiros e crie dois sets com essas listas. 
#Em seguida, determine e exiba os números que estão 
#presentes nos dois sets (interseção).

def obter_lista_numeros_int():
    numeros1 = input("Digite três números inteiros com espaço: ")
    numeros2 = input("Digite três números inteiros com espaço: ")
    lista1 = [int(numero) for numero in numeros1.split()]
    lista2 = [int(numero) for numero in numeros2.split()]
    return set(lista1), set(lista2)

def sets():
    set1, set2 = obter_lista_numeros_int()
    print(f"Lista 1 (Set 1): {set1}")
    print(f"Lista 2 (Set 2): {set2}")

    intersecao = set1.intersection(set2)
    print(f"Interseção: {intersecao}")

sets()

