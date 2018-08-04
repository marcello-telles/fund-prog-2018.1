def lerVetor(n):
    vetor = []
    for i in range(n):
        vetor.append(input())
    return vetor


def lerValor():
    return input()


def buscaBinaria(lista, valor):
    posValor = -1
    posPrimeiro = 0
    posUltimo = len(lista)-1

    while posUltimo >= posPrimeiro and posValor == -1:
        posMeio = (posUltimo + posPrimeiro) // 2
        if lista[posMeio] == valor:
            posValor = posMeio
        else:
            #se o valor for menor que o elemento do meio, pega a metade à esquerda
            #portanto a ultima posicao passa a ser o meio - 1
            if lista[posMeio] > valor:
                posUltimo = posMeio - 1
            else:
                posPrimeiro = posMeio + 1
    return posValor


n = int(input())
vetor = lerVetor(n)
busca = buscaBinaria(vetor, lerValor())
if busca > -1:
    print("O valor foi encontrado na posição %d" % busca)
else:
    print("O valor não foi encontrado")