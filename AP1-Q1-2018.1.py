def bissexto(a):
    return a % 4 == 0 and not (a % 100 == 0 and a % 400 != 0)


ano = int(input())
while ano > 0:
    if bissexto(ano):
        print("O ano %d é bissexto" % ano)
    else:
        print("O ano %d não é bissexto" % ano)
    ano = int(input())