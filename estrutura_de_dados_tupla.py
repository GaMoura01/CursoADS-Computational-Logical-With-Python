#Manipulando tuplas - tuple 

cores = ("vermelha", "azul", "amarelo", "verde")

print(f"Meu carro é {cores [1]}")

qtd = len(cores)
print(f"Tenho {qtd} de opções de cores")

cor = input("Digite uma cor: ")
if cor in cores:
    qtd_cor = cores.count(cor)
    print (f"Temos {qtd_cor} tipo de {cor}")  
else: 
    print(f"A cor {cor} não existe na loja")


aluno = ("Gabriella", 10, 5)
nome, nota1, nota2 = aluno 
media = (nota1 +nota2) / 2

print(f"O aluno {nome} com as notas {nota1} e {nota2} está com a média {media}")