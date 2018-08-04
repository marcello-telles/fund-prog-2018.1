def padovan(n):
    if n <= 2:
        return 1
    else:
        return padovan(n-2) + padovan(n-3)


num = int(input())
while num >= 0:
    print(padovan(num))
    num = int(input())
