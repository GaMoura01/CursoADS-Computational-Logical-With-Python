#4. Escreva um programa que solicite 
#um número ao usuário e determine se 
#ele é divisível por 5.

#Solicito que o usuário informe um número de sua escolha:

numero = int(input("Digite um número: "))

#Faço o controle, o operador % retorna o resto da divisão entre dois números. 
#O código 'numero % 5 == 0' verfica se o resto da divisão do numero por 5 é igual a zero,
#isso indica que o número é divisível por 5, e o resultado é exibido. 
#Caso contrário, nada é exibido.

if numero % 5 == 0:
    print("O número é divisivel por 5. ")

else: 
    print("O número não é divisivel por 5. ")

#Após o resultado, será dado como final do programa.

print("Fim do programa!")

