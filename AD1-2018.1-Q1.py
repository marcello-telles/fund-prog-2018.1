numeros = []
entrada = int(input('Insira o numero: '))
while entrada >= 0:
    if len(numeros) < 5:
        numeros.append(entrada)
    else:
        menor = min(numeros)
        if entrada > menor:
            numeros[numeros.index(menor)] = entrada
    entrada = int(input('Insira o numero: '))

numeros.sort(reverse=True)
for x in numeros:
    print(x, end=" ")
