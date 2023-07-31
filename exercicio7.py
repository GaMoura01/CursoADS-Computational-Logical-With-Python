#Crie um programa que solicite as notas e a 
#frequência de um aluno, e determine sua situação. 
#Se a média for maior ou igual a 5 e a frequência 
#for maior ou igual a 75%, o aluno está aprovado. 
#Se a média for menor que 5 e a frequência for menor 
#que 75%, o aluno está reprovado. Em qualquer outro 
#caso, o aluno está de recuperação.

#Solicito que o usuário informe a nota/media do aluno e frequência.

nota_aluno = float(input("Digite a nota do aluno: "))
frequencia_aluno = int(input("Digite a frequência do aluno: "))

#Faço o controle, se a nota/media do aluno for maior ou igual a 5 e sua frequência maior ou igual a 75,
#o aluno está aprovado. Se sua nota/média for maior ou igual a 5 OU sua frequência maior ou igual a 75,
#o aluno está de recuperação. Fora destes padrões, o aluno está reprovado.

if nota_aluno >= 5 and frequencia_aluno >= 75:
    situacao = "aprovado!"


elif nota_aluno >= 5 or frequencia_aluno >= 75:
    situacao = "de recuperação!"

else:
    situacao = "reprovado!"

#Código para exibir o resultado: 

print(f"O aluno está {situacao}")

#Após o resultado, será dado como final do programa. 

print("Fim do programa")
