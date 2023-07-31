#3. Crie um programa que solicite um número
#ao usuário e determine se ele é positivo, 
#negativo ou zero.

#Solicito que o usuário informe um número de sua escolha:

numero = int(input("Digite um número: "))

#Faço o controle, se o número informado for maior que 0, o número é positivo. 
#Se o número informado for menor que 0, o número é negativo. 
#Fora destes padrões, o número é zero.

if numero > 0:
    print(f"O {numero} é positivo!")

elif numero < 0: 
    print(f"O {numero} é negativo!")

else: 
    print("O numero é zero")

#Após o resultado, é dado como final do programa.

print("Fim do programa!")
