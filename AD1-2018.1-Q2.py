# encoding: utf-8
import unicodedata
def contaVogais(v):
    soma = 0
    vogais = 'AaEeIiOoUu'
    for i in v:
        for j in vogais:
            soma += unicodedata.normalize('NFKD', i).count(j)
    return soma


def contaDigitos(v):
    soma = 0
    for i in v:
        for j in range(10):
            soma += i.count(str(j))
    return soma


def maiorString(v):
    tam, string = 0, ""
    for j in v:
        if len(j) > tam:
            tam = len(j)
            string = j
    return string


def contaPalindromos(v):
    soma = 0
    for i in v:
        if i == i[::-1]:
            soma += 1
    return soma


strings = []
entrada = input('Entre com a string: ')
while entrada != "":
        strings.append(entrada)
        entrada = input('Entre com a string: ')

print('Vogais lidas: %d' % contaVogais(strings))
print('Dígitos lidos: %d' % contaDigitos(strings))
print('Maior string: %s' % maiorString(strings))
print('Palíndromos lidos: %s' % contaPalindromos(strings))
