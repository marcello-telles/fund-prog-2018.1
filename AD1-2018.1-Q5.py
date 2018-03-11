# encoding: utf-8
import math


def distEntrePontos(par1, par2):
    return math.sqrt((par1[0] - par2[0])**2 + (par1[1] - par2[1])**2)


def calculaMaisProximos(v):
    pontoA, pontoB = v[0], v[1]
    menorDist = distEntrePontos(v[0], v[1])
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            dist = distEntrePontos(v[i], v[j])
            if dist < menorDist:
                menorDist = dist
                pontoA, pontoB = v[i], v[j]

    print('Os pontos mais próximos entre si são', pontoA, 'e', pontoB)
    return None


def calculaMaisDistantes(v):
    pontoA, pontoB = v[0], v[1]
    maiorDist = distEntrePontos(v[0], v[1])
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            dist = distEntrePontos(v[i], v[j])
            if dist > maiorDist:
                maiorDist = dist
                pontoA, pontoB = v[i], v[j]

    print('Os pontos mais distantes entre si são', pontoA, 'e', pontoB)
    return None


def mediaCoord(v):
    somaX, somaY = 0, 0
    for i in range(len(v)):
        somaX += v[i][0]
        somaY += v[i][1]
    print('A média de x é %.3f e a média de y é %.3f' % (somaX / len(v), somaY / len(v)))
    return None


pares, vetor = [], [1, 1]
x, y = map(int, input('Entre com o par: ').split())
while not (x == 0 and y == 0):
    pares.append((x, y))
    x, y = map(int, input('Entre com o par: ').split())
print('Número de pares válidos lidos: %d' % len(pares))
print('Os pontos são:')
for x in pares:
    print(x)
calculaMaisProximos(pares)
calculaMaisDistantes(pares)
mediaCoord(pares)
