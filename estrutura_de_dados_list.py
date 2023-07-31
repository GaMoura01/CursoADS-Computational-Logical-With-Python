#Manipulando listas - list 

#Criando uma lista

#Adicionando nomes com o FOR 
nomes = ["Ana", "Pedro"]
print(f"Lista original: {nomes}")

for cont in range(1):
    novo_nome = input(f"Digite um nome {cont}: ")
    nomes.append(novo_nome)
print(f"Lista adicionando 1 nomes: {nomes}")

#Adicionndo N quantidade de nomes com WHILE

resp = "s"
while resp == "s":
    novo_nome = input(f"Digite um nome: ")
    nomes.append(novo_nome)
    resp = input("Deseja cadastrar mais um nome [s/n]: ")
print(f"Lista adicionando n nomes: {nomes}")

#Listando elementos pela posição 

print(nomes[0])

#Removendo o ultimo elemento da lista

nomes.pop()
print(f"Removendo o ultimo: {nomes}")

#Removendo um elemento qualquer:

nomes.remove("Pedro")
print(f"Removendo um elemento: {nomes}")

#Verificando a existencia de um elemento

nome_pesquisado = input("Digite um nome para pesquisar: ")
if nome_pesquisado in nomes:
    print("Nome cadastrado")
else:
    print("Nome não cadastrado")