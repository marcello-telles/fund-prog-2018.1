def parseFloat(vet):
    for k in range(len(vet)):
        vet[k] = float(vet[k])
    return vet


def trocaPos(dic, posA, posB):
    tmp = dic.get(posA)
    dic[posA] = dic.get(posB)
    dic[posB] = tmp
    return None


def calculaMedia(medias, p):
    valMedia = 0
    for k in range(len(medias)):
        valMedia += medias[k]*p[k]
    valMedia /= 10
    return valMedia


def desempatePossivel(dic, chaveA, chaveB, posA, posB):
    return dic.get(posA).get(chaveB) == dic.get(posB).get(chaveB)\
           and dic.get(posA).get(chaveA) != dic.get(posB).get(chaveA)


def ordenaMedia(cand):  # bubble sort decrescente
    tam = len(cand)-1
    for k in range(tam):
        trocou = False
        for j in range(tam-k):
            if cand.get(j).get('media') < cand.get(j+1).get('media'):
                trocou = True
                trocaPos(cand, j, j+1)
        if not trocou:
            break
    return None


def desempateIdade(cand):
    tam = len(cand) - 1
    for k in range(tam):
        trocou = False
        for j in range(tam - k):
            if desempatePossivel(cand, 'idade', 'media', j, j+1):
                if cand.get(j).get('idade') < cand.get(j+1).get('idade'):
                    trocou = True
                    trocaPos(cand, j, j+1)
        if not trocou:
            break
    return None


def desempateNome(cand):
    tam = len(cand) - 1
    for k in range(tam):
        trocou = False
        for j in range(tam - k):
            if desempatePossivel(cand, 'nome', 'idade', j, j+1):
                if cand.get(j).get('nome') > cand.get(j+1).get('nome'):
                    trocou = True
                    trocaPos(cand, j, j+1)
        if not trocou:
            break
    return None


pesos = parseFloat(input().split())
qtd = int(input())
candidatos = dict()
for i in range(qtd):
    linha = input().split()
    candidatos[i] = {'nome': linha[0], 'idade': int(linha[1]), 'media': calculaMedia(parseFloat(linha[2:]), pesos)}

ordenaMedia(candidatos)
desempateIdade(candidatos)
desempateNome(candidatos)

for x in candidatos:
    print(candidatos.get(x).get('nome'))
