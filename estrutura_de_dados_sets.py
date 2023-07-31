#Manipulando conjuntos - sets

usuarios = {"Ana", "Maria"}
usuarios.add("Felipe")
print(usuarios)

#verificando se o elemento existe:

usuario_digitado = input("Digite seu usuario: ")
if usuario_digitado in usuarios:
    print(f"Usuario cadastrado")
else:
    print("Usuario não cadastrado")

#Verificando conjuntos: UNION = junta todos

novos_usuarios = {"Felipe", "Pedro", "Mario"}

print(usuarios)
print(novos_usuarios)

todos_usuarios = usuarios.union(novos_usuarios)

print(f"União: {todos_usuarios}")

#Verificando conjuntos: INTERSECTION = junta os semelhantes/comuns

usuarios_comuns = usuarios.intersection(novos_usuarios)
print(f"Interseção: {usuarios_comuns}")

#verificando diferenças: DIFFERENCE 

usuarios_diferentes = usuarios.difference(novos_usuarios)
print(f"Diferença: {usuarios_diferentes}")