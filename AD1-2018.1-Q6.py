# encoding: utf-8
def converte(decimal, base):
    if decimal >= 0 and (9 >= base >= 2):
        result, num = "", decimal
        if num >= base:
            while num > 0:
                resto = num % base
                num = num // base
                result += str(resto)
            print(result[::-1])
        else:
            print(str(num))
        num, base = map(int, input('Digite número e base:').split())
        converte(num, base)
    return None


dec, b = map(int, input('Digite número e base:').split())
converte(dec, b)