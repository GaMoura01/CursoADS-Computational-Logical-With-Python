#Faça um programa que solicite um número ao 
#usuário e exiba a tabuada desse número de 1 a 10.

#Solicito que o usuário informe um número de sua escolha:

numero = int(input("Digite um número: "))

#Faço o controle, onde o range() cria a sequência de números. A sequência 
#é percorrida pelo 'for', onde a variável i assume o valor da sequência a cada iteração.
#A variável resultado faz a multiplicação da sequência e o resultado é exibido.

for i in range(1,11):
    resultado = numero * i
    print (f"{numero} X {i} = {resultado}")

#Após o resultado, será como dado final do programa

print("Fim do programa!")