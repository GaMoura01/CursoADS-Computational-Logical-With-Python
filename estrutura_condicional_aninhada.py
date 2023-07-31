anos_experiencia = int(input("Digite os anos de experiencia: "))

if anos_experiencia == 0:
    nivel = "estagiario"
elif anos_experiencia <= 3:
    nivel = "junior"
elif anos_experiencia <= 8:
    nivel = "pleno"
else: 
    nivel = "senior"

print (f"Voce é um desenvolvedor do nível: {nivel}")
