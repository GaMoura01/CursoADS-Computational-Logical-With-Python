#Crie um programa que solicite um número ao 
#usuário e calcule o fatorial desse número.

#Solicito que o usuário informe um número de sua escolha.
#O fatorial é uma operação matemática que consiste em multiplicar 
#um número inteiro positivo por todos os seus antecessores até o número 1.

numero = int(input("Digite um número: "))

fatorial = 1

#Faço o controle, se o número informado for negativo, ex: -9,
#o fatorial não poderá ser definido. Se o número informado for igual a 0,
#o fatorial é 1. 
#É feito um controle de fluxo, onde o range () cria a sequência de números. A sequência 
#é percorrida pelo 'for', onde a variável i assume o valor da sequência a cada iteração.
#O variável fatorial faz a multiplicação da sequência e o resultado é exibido.

if numero < 0:
    print("O fatorial de um número negativo não definido.")
    
elif numero == 0:
    print("O fatorial de 0 é 1.")
    
else:
    for i in range(1, numero + 1):
     fatorial *= i

print(f"O fatorial de {numero} é {fatorial}.")

#Após o resultado, será dado como final o programa. 

print("Fim do programa!")



