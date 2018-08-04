def fatorial_duplo(n):
    if n > 1:
        return n*fatorial_duplo(n-2)
    else:
        return n

num = int(input())
while num >= 0:
    if num % 2 == 0:
        print("O número %d é par" % num)
    else:
        print("O fatorial duplo de %d é %d" % (num, fatorial_duplo(num)))
    num = int(input())
