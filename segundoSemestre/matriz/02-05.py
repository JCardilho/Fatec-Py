#Faça um programa que preencha uma matriz 2 x 4, calcule e mostre:
 #◦a quantidade de elementos pares
 #◦a soma dos elementos ímpares
from random import randint
matriz=[]
linha=[]
quant=0
somaimp=0
for c in range(2):
    linha=[]
    for l in range (4):
        linha.append (randint(1,100))
        if linha[l] %2==0:
            quant+=1
        else:
            somaimp+=linha[l]	         
    matriz.append(linha)
print (matriz)
        
print(f"a quantidade de elementos pares :{quant}")
print (f"a soma dos elementos ímpares:{somaimp} ")
