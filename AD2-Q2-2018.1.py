def ultInd(dado):
    return len(dado)-1


def corrigePalavra(pal):
    fimLista = ultInd(pal)
    string = pal[fimLista]
    for k in range(fimLista, int(fimLista/2), -1):  # laco do ultimo indice ao meio da lista
        if string == pal[k-len(string):k]:
            pal = pal.replace(string, "", 1)
            break
        string = pal[k-1]+string
    return pal


with open("mensagens_originais.txt", "r") as arqOrigem:
    with open("mensagens_corrigidas.txt", "w") as arqDestino:
        qtd = int(arqOrigem.readline())
        for i in range(qtd):
            corrigidas, escrever = 0, []
            linha = arqOrigem.readline()
            palavras = linha.split()
            for palavra in palavras:
                correcao = corrigePalavra(palavra)
                escrever.append(correcao)
                if correcao != palavra:
                    corrigidas += 1
            arqDestino.write(str(corrigidas))  # numero de corrigidas
            for x in escrever:
                arqDestino.write(" "+x)  # escreve as correcoes (ou nao correcoes)
            arqDestino.write("\n")  # pula linha
