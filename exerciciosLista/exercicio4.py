lista_palavras_ingles = []
lista_palavras_pt = []

resp = 1

while (resp !=0 ):
    lista_palavras_ingles.append(input("Digite uma palavra em inglês: "))
    lista_palavras_pt.append(input("Digite uma palavra em portugues: "))

    resp = int(input("Deseja prosseguir? (1-SIM ou 0-NÃO)?: "))

palavra_ingles = input("Digite a palavra em inglês que será traduzida: ")

if (palavra_ingles in lista_palavras_ingles):
    posicao_palavra = lista_palavras_ingles.index(palavra_ingles)
    print(f"A palabra em português é {lista_palavras_pt[posicao_palavra]}")