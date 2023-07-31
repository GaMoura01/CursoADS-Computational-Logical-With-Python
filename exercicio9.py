#Crie um programa que solicite três medidas de 
#retas ao usuário e determine se essas medidas 
#podem formar um triângulo.

#Solicito que o usuário forneça três medidas 
#(elas podem ser numeros inteiros ou numeros reais, ex 7.5):

lado1 = float(input("Digite a medida do primeiro lado: "))
lado2 = float(input("Digite a medida do segundo lado: "))
lado3 = float(input("Digite a medida do terceiro lado: "))

#Faço o controle, se a soma de quaisquer dois lados é maior que 
#o terceiro lado, caso for, pode formar um triangulo,
#caso não for, não pode formar um triangulo. 

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("As medidas podem formar um triângulo!")

else: 
    print("As medidas não podem formar um triângulo!")

#Após o resultado, será dado como fim do programa. 

print("Fim do programa!")

