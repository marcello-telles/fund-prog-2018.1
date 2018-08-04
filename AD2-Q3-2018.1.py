def montaDicionario(lista):  # retorna um dict onde as chaves sao os elementos da lista e os valores sao 0
    dic = dict()
    for x in lista:
        dic[x] = 0
    return dic


def lePalavras(ponteiro):  # retorna o conjunto de palavras
    stringPalavras = ""
    conjunto = set()
    for pal in ponteiro:
        plvr = pal.replace("\n", "")
        conjunto.add(plvr)
        stringPalavras += " "+plvr
    stringPalavras = stringPalavras.replace("-\n", "")
    return conjunto, montaDicionario(stringPalavras.split())


def leDiscurso(ponteiro):  # retorna uma lista com as palavras do discurso
    stringDiscurso = ""
    for linha in ponteiro:
        stringDiscurso += "".join(linha)
    stringDiscurso = stringDiscurso.replace("-\n", "")
    return stringDiscurso.split()


def contaPalavras(pal, dis, cont):
    for p in pal:
        for d in dis:
            if p == d:
                cont[p] += 1
    return None


with open("palavras.txt", "r") as arqPalavras:
    palavras, contagem = lePalavras(arqPalavras)

with open("discurso.txt", "r") as arqDiscurso:
        discurso = leDiscurso(arqDiscurso)

contaPalavras(palavras, discurso, contagem)
with open("contagem.txt", "w") as arqContagem:
    for i in contagem:
        arqContagem.write(i+" "+str(contagem[i])+"\n")
