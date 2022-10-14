#faça um programa que leia 10 numeros inteiros e armazene os na lista A
# encntre  o menor numero da lista A e gere a lista B que é a multiplicação de cada elemento da lista aA pelo menor numero
# gere a lista C que é a união da lista A e a B
# mostre as 3 lista na tela
listaA=[]
listaB=[]
listaC=[]

from random import randint

for i in range (10):
    listaA.append(randint(0,100))
menor=min(listaA)    
for i in range(len(listaA)):
    listaB.append (listaA[i]*menor)

listaC=listaA+listaB
               


print (listaA)
print (listaB)
print (listaC)
