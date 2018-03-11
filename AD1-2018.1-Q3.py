# encoding: utf-8
qtd = int(input('Definição do Pleito:\n'))
i, candidatos, votos = 0, [], []
for i in range(qtd):
    candidatos.append(input())
    votos.append(0)

print('')
print('Votação:', end='\n')

vt = input()
while vt in candidatos:
    votos[candidatos.index(vt)] += 1
    vt = input()

for j in range(len(candidatos)):
    print('%s com %d voto(s)' % (candidatos[j], votos[j]))
