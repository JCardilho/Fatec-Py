#Faça um programa que preencha uma matriz 2 x 4, calcule e mostre: 
# a quantidade de elementos pares e a soma dos elementos ímpares

from random import randint
coluna=[]
quantpar=0
somaim=0
lispar=[]
lisim=[]
for c in range (2):
    linha=[]
    for l in range (4):
        linha.append(randint(0,100))
        if linha [l] %2==0:
            quantpar+= 1
            lispar.append(linha[l])
        else:
            somaim+= linha[l]
            lisim.append(linha[l])
    coluna.append(linha)
for i in range (2):
    print (coluna[i])
print (f"a quantidade de elementos pares são: {quantpar}:{lispar}" )   
print (f"a soma dos elementos ímpares são : {somaim}::{lisim}")
    
