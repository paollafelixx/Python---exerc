lista_numeros = []
qt_mult3 = 0

for i in range(10):
    lista_numeros.append(int(input("Digite um numero: ")))

for i in range(10):
    if (lista_numeros[i] % 3 == 0):
        qt_mult3+=1

print(f"Quantidade de numeros multiplos de 3 na lista: { qt_mult3}")