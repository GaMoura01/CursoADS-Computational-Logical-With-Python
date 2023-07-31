#2. Faça um programa que solicite dois
#números ao usuário e exiba o maior deles.

#Solicito que o usuário informe dois números de sua preferência:

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

#Faço o controle, se o primeiro número informado for maior que o segundo, 
#será exibido uma mensagem que confirma a informação. Se o segundo número informado
#for maior que o primeiro, será exibido uma mensagem que confirme a informação.
#Fora destes padrões, os números informados são iguais.

if numero1 > numero2:
    print(f"O {numero1} é maior que o {numero2}.")

elif numero2 > numero1:
    print(f"O {numero2} é maior que o {numero1}.")

else: 
    print(f"O {numero1} e o {numero2} sào iguais.")

#Após o resultado, será dado como final do programa.

print("Fim do programa!")