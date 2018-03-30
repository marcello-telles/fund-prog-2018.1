def mediasChuva(lista, intervalo):
    medias = []
    for i in range(intervalo-1,len(lista)):
        soma = 0
        for j in range(intervalo):
            soma += lista[i-j]
        medias.append(soma / intervalo)
    return medias


cidade = 1
inp = input().split()
qtd, interv = int(inp[0]), int(inp[1])
while qtd > 0 and interv > 0:
    lista = []
    for i in range(qtd):
        lista.append(int(input()))
    med = mediasChuva(lista, interv)
    print("Cidade %d" % cidade)
    print("%.2f %.2f" %(min(med), max(med)))
    print()
    cidade += 1
    inp = input().split()
    qtd, interv = int(inp[0]), int(inp[1])
