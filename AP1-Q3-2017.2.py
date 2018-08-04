import random


def geraMatriz(l, c):
    mtz = []
    for i in range(l):
        vetor = []
        for j in range(c):
            vetor.append(random.randint(0, 9))
        mtz.append(vetor)
    return mtz


def mediaMatriz(mtz):
    soma, contador = 0, 0
    for i in range(len(mtz)):
        for j in range(len(mtz[i])):
            soma += mtz[i][j]
            contador += 1

    return soma / contador


def linhaMedia(mtz, media):
    vetor = []
    for i in range(len(mtz)):
        maiorQueMedia = True
        for j in range(len(mtz[i])):
            if mtz[i][j] <= media:
                maiorQueMedia = False
                break
        if maiorQueMedia:
            vetor.append(i)
    return vetor


lin, col = map(int, input().split())
matriz = geraMatriz(lin, col)
for x in matriz:
    for z in x:
        print(z, end=" ")
    print()
print()
media = mediaMatriz(matriz)
print(media)
print()
for x in linhaMedia(matriz, media):
    for z in matriz[x]:
        print(z, end=" ")
    print()