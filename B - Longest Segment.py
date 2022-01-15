import math

def func(*pontos):
    return math.sqrt(((pontos[1][0]-pontos[0][0])**2) + ((pontos[1][1]-pontos[0][1])**2))
N = int(input())
pontos = []

for i in range(N):
    entrada = input().split(' ')
    pontos.append((float(entrada[0]), float(entrada[1])))

distanciaMaior = 0

for e, i in enumerate(pontos):
    for en, j in enumerate(range(N - e - 1)):
        dist = func(i, pontos[e+1+en])
        if distanciaMaior < dist:
            distanciaMaior = dist
print(distanciaMaior)
