#Escreva um programa em Python que preencha uma matriz de ordem 5 x 5 com número
#inteiros e mostre na tela a matriz preenchida. (2 pts)
#Calcule e mostre na tela:
#• o maior número da coluna 2, ou seja, índice 1; (1,5 pts)
#• a média dos números da 4ª linha da matriz, ou seja, índice 3; (1,5 pts)
#• a quantidade de números da matriz que são pares, e maiores ou iguais a 10
#e menores ou iguais a 15; (1,5 pts)
#• faça a média dos números de cada linha da matriz e armazene em uma lista. (2 pts)
#Obs: entregar o arquivo .py

from random import randint
matriz=[]
cont=0
quant=0
soma5=soma4=0
listamed=[]
mediama=0

for l in range(5):
    linha=[]
    for c in range (5):
        linha.append(randint(1,100))
    matriz.append(linha)
maior2=matriz[4][1]
for j in range (5):
    for k in range (5):
        if j==3:
            soma4+=matriz[3][k]
        if matriz[j][k] % 5==0:
            soma5+= matriz[j][k]
            cont+=1
        if matriz[j][1] > maior2:
            maior2=matriz[j][1]
        
        if matriz[j][k]>=10 and  matriz[j][k]<=15:
            num=matriz[j][k]
            if num %2==0:
                quant+=1
                            
for i in matriz:
    print(i)
print("-="*30)
print (f"A média dos números múltiplos de 5; {soma5/cont}")
print(f"o maior número da coluna 2, ou seja, índice 1;{maior2}")
print(f"a média dos números da 4ª linha da matriz, ou seja, índice 3;{soma4/5}")
print(f"a quantidade de números da matriz que são pares, e maiores ou iguais a 10 e menores ou iguais a 15;{quant}")
print("-="*30)
for m in range(5):
    mediama=0
    for n in range (5):
        mediama += matriz[m][n]
    listamed.append(mediama/5)
for o in range (5) :
    print(f"a média dos números da linha : {o+1}  {listamed[o]}")
