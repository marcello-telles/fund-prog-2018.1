import struct


def montaArquivo():
    try:
        v = [(-9, 20.5), (6, 10.8), (10, 8.0), (45, -99.6), (12, -54.7)]
        with open("valores.bin", "wb") as arq:
            arq.write(struct.pack("=i", len(v)))
            for tupla in v:
                arq.write(struct.pack("=i", tupla[0]))
                arq.write(struct.pack("=f", tupla[1]))
    except IOError:
        print("Erro ao abrir ou manipular o arquivo na função")


def leArquivo():
    try:
        with open("valores.bin", "rb") as arq:
            n = struct.unpack("=i", arq.read(4))[0]
            print(n, end=" ")
            for k in range(n):
                print(struct.unpack("=i", arq.read(4))[0], end=" ")
                print(round(struct.unpack("=f", arq.read(4))[0], 4), end=" ")
    except IOError:
        print("Erro ao abrir ou manipular o arquivo na função")


try:
    entradaInt = int(input())
    entradaFloat = float(input())
    montaArquivo()
    leArquivo()
    with open("valores.bin", "r+b") as arq:
        qtd = struct.unpack("=i", arq.read(4))[0]
        for i in range(qtd):
            inteiro = struct.unpack("=i", arq.read(4))[0]
            if inteiro < entradaInt:
                # volta o ponteiro 4 bytes e substitui o dado por -1
                arq.seek(-4, 1)
                arq.write(struct.pack("=i", -1))
            # arq.seek(4, 1)
            flutuante = round(struct.unpack("=f", arq.read(4))[0], 4)
            if flutuante > entradaFloat:
                # volta o ponteiro 4 bytes e substitui o dado por 9999.0
                arq.seek(-4, 1)
                arq.write(struct.pack("=f", 9999.0))

    print()
    leArquivo()

except IOError:
    print("Erro ao abrir ou manipular o arquivo")
