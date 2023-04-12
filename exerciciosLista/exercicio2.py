lista_idades = []

soma_idades = 0
qt_menores18 = 0

idade = int(input("Digite a idade atual do usuario: "))

while (idade > 0):
    lista_idades.append(idade)
    idade = int(input("Digite a idade do usuario: "))

for i in range(len(lista_idades)):
    soma_idades+=lista_idades[i]
    if (lista_idades[i < 18]):
        qt_menores18+=1

media = soma_idades / len(lista_idades)  # Outra forma de resolver: sum(lista_idades) / len(lista_idades)

print(f"A média das idades: {media:.2f}")
print(f"A quantidade de usuarios menores de 18 anos: {qt_menores18}")