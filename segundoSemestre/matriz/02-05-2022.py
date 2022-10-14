#Faça um programa que leia duas matrizes A e B 2x2 de inteiros 
#e imprima a matriz C que é a soma das matrizes A e B.

from random import randint
matrizA=[]

matrizB=[]
matrizC=[]
for c in range (2):
    linha=[]
    linha1=[]
    for l in range (2):
        linha.append (randint(1,100))
        linha1.append (randint(1,100))
    matrizA.append(linha)
    matrizB.append (linha1)

for i in range (2):
    for j in range (2):
        matrizC.append ( matrizA [i][j]+matrizB [i][j])
print (matrizA)
print (matrizB)
print (matrizC)
