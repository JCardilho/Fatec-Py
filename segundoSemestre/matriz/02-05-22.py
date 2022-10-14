#Faça um programa que preencha uma matriz 3 x 4, calcule e mostre:
#◦A média de todos os elementos
#◦A quantidade de elementos maiores que a média

from random import randint
matriz=[]
media=maiormed=0
soma=0
for c in range (3):
    linha=[]
    for l in range (4):
        linha.append (randint(1,100))
        soma+= linha[l]
    matriz.append(linha)
media = soma/12
print(matriz)
for i in range (3):
    for j in range (4):
        if matriz[i][j] > media :
            maiormed+=1       

print (f"A média de todos os elementos:{media}")
print (f"A quantidade de elementos maiores que a média{maiormed}")
