#faça um programa que preencha uma lista com 10 numeros inteiros
# calcule o fatorial de cada numero e armazene em uma lista
# imprima um relatorio na tela mstrando o numero e o fatorial dele

	
	
from random import randint
lista1=[]
lista2=[]
fat=[]
	
for i in range (0,10):
    lista1.append (randint(1,8))
    print (lista1)
for i in range (0,10):
    fat =1
    for k in range (2,lista1[i]+1):
        fat=fat*k
    lista2.append( fat)
for i in range (0,10):
    print("O numero ",  lista1[i], "Seu fatorial é :", lista2[i])
