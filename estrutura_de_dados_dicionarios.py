#Manipulando dicionarios 

cliente = {
    "nome": "Gabriella", 
    "cidade": "São Paulo",
    "ano_nasc": 2004,
    "ativo": False
}
print(cliente["nome"])

#Atualizar um dado:

cliente["ano_nasc"] = 2000

print(cliente)

#Deletar um dado 

del cliente ["cidade"]

print(cliente)

#Pesquisar dados:

if "ano_nasc" in cliente:
    print(f"O cliente nasceu em {cliente['ano_nasc']}")
else:
    print("Não existe a chave ano_nasc")

print(f"Lista de valores: ")

for valor in cliente.values():
    print(valor)

print(f"Lista de chaves: ")

for chave, valor in cliente.items():
    print(chave)