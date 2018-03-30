def divisores(n):
    vetor = []
    for i in range(1, n):
        if n % i == 0:
            vetor.append(i)
    return vetor


def somaVetor(v):
    soma = 0
    for i in v:
        soma += i
    return soma


def perfeito(n):
    div = divisores(n)
    return somaVetor(div) == n


num = int(input())
while num > 0:
    if perfeito(num):
        print("O número %d é perfeito" % num)
    else:
        print("O número %d não é perfeito" % num)
    num = int(input())
