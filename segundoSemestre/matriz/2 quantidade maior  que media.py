#Faça um programa que preencha uma matriz 3 x 4, calcule e mostre:
#◦ A média de todos os elementos
#◦ A quantidade de elementos maiores que a média

from random import randint
coluna=[]
linha=[]
maiormedia=[]
cont=media=soma=0
for c in range(3):
    linha=[]
    for l in range(4):
        linha.append(randint(0,100))
        soma+= linha[l]
    coluna.append(linha)

media= soma/12
for i in range (len(coluna)):
    for j in range (len(linha)):
        if coluna [i][j] > media:
            cont+=1
            maiormedia.append(coluna [i][j])
            
print (f"A média de todos os elementos:{media}")
print (f"A quantidade de elementos maiores que a média são: {cont};;{maiormedia}")
          
