#Crie um programa que solicite ao usuário o início, 
#o fim e o número para a tabuada. 
#Em seguida, exiba a tabuada desse número no 
#intervalo determinado.

#Solicito que o usuário informe o numero de sua escolha para a tabuada, o inicio e o fim do intervalo:

numero = int(input("Digite um número: "))
inicio_intervalo = int(input("Digite o inicio do intervalo: "))
fim_intervalo = int(input("Digite o fim do intervalo: "))

#Efetuo um controle de fluxo que permite iterar sobre sequência de números. O range() cria
#uma sequência de números do inicio e vai até o fim. A sequência é percorrida pelo 'for', onde
#a variável i assume o valor da sequência a cada iteração. O 'resultado' calcula o resultado da 
#multiplicacão do numero infomado pelo valor atual de i. O print exibe o resultado.

for i in range (inicio_intervalo, fim_intervalo + 1): 
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#Após o resultado, será dado como final do programa

print("Fim do programa!")