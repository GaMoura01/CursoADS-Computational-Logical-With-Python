#1. Escreva um programa que solicite um número 
#ao usuário e verifique se ele é par ou ímpar.

#Solicito que o usuário informe um número de sua escolha:

numero = int(input("Digite um número: "))

#Faço o controle, o operador % retorna o resto da divisão entre dois números. 
#O código numero % 2 == 0 verifica se o resto da divisão do número por 2 é igual a zero,
#o que indica que o número é par, e uma mensagem será exibida confirmando a informação.
#Fora deste padrão, o número informado será ímpar e será eibida uma mensagem confirmando
#a informação.

if numero % 2 == 0:
    print("Par")

else:
    print("Ímpar")

#Após o resultado, será dado como final do programa.

print("Fim do programa!")
