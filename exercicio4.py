#Elabore um programa que leia quatro valores inteiros 
# (variáveis A, B, C e D). Ao final, o programa deve 
# apresentar o resultado do produto (variável P) 
# do primeiro com o terceiro valor, e o resultado 
# da soma (variável S) do segundo com o quarto valor.

c = input("Digite o valor de C: ")
d = int(input("Digite o valor de D: "))
e = int(input("Digite o valor de E: "))
f = int(input("Digite o valor de F: "))

P = c * e
S = d + f

print(f"Produto de C e E é: {P}")
print(f"A soma de D e F é: {S}")