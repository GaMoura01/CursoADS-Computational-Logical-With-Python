nota = float(input("Digite sua nota: "))
frequencia = int(input("Digite sua frequencia: "))

if nota >= 5 and frequencia >= 75:
    situacao = "aprovado!"
elif nota >= 5 or frequencia >= 75: 
    situacao = "de recuperacao!"
else:
    situacao = "reprovado!"

print(f"Voce esta {situacao}")
