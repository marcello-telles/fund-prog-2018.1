# encoding: utf-8
import random

def maiorValor(mtz):
    maiorValMatriz, linMaior, colMaior = valMinimo, 0, 0
    for g in range(len(mtz)):
        for h in range(len(mtz[g])):
            if mtz[g][h] > maiorValMatriz:
                maiorValMatriz = mtz[g][h]
                linMaior = g
                colMaior = h
    return [maiorValMatriz, linMaior, colMaior]


def multMaiorCadaLinha(mtz):
    vetor, result = [], 1
    for g in range(len(mtz)):
        maiorValLinha = valMinimo
        for h in range(len(mtz[g])):
            if mtz[g][h] > maiorValLinha:
                maiorValLinha = mtz[g][h]
        vetor.append(maiorValLinha)
    for g in vetor:
        result *= g
    return result


def somaMenorCadaLinha(mtz):
    vetor, result = [], 0
    for g in range(len(mtz)):
        menorValLinha = valMaximo
        for h in range(len(mtz[g])):
            if mtz[g][h] < menorValLinha:
                menorValLinha = mtz[g][h]
        vetor.append(menorValLinha)
    for g in vetor:
        result += g
    return result


def linhaMaiorIntervalo(mtz):
    vetor, linha, result = [], 0, 0
    for g in range(len(mtz)):
        menorValLinha = valMaximo
        maiorValLinha = valMinimo
        for h in range(len(mtz[g])):
            if mtz[g][h] < menorValLinha:
                menorValLinha = mtz[g][h]
            if mtz[g][h] > maiorValLinha:
                maiorValLinha = mtz[g][h]
        vetor.append(abs(maiorValLinha-menorValLinha))
    for g in range(len(vetor)):
        if vetor[g] > result:
            result = vetor[g]
            linha = g
    return [result, linha]


numLinhas = int(input('Entre com a quantidade de linhas: '))
numCols = int(input('Entre com a quantidade de colunas: '))
valMinimo = int(input('Entre com o valor mínimo: '))
valMaximo = int(input('Entre com o valor máximo: '))
matriz = []
for i in range(numLinhas):
    vetorTmp = []
    for j in range(numCols):
        vetorTmp.append(round(random.uniform(valMinimo, valMaximo), 3))
    matriz.append(vetorTmp)

print('A matriz é:')
for x in matriz:
    print(x)
maior = maiorValor(matriz)
intervalo = linhaMaiorIntervalo(matriz)
print('O maior valor é %.3f, na linha %d e coluna %d' % (maior[0], maior[1], maior[2]))
print('O produto dos maiores valores de cada linha é %.3f' % multMaiorCadaLinha(matriz))
print('A soma dos menores valores de cada linha é %.3f' % somaMenorCadaLinha(matriz))
print('A linha de maior intervalo entre o maior e o menor valor é a linha %d (%.3f)' % (intervalo[1], intervalo[0]))
