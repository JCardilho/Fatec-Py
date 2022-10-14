# faça um programa que leia 10 numeros inteiros e armazene os numeros pares na
#lista par eos numeros impares na lisra impar imprima as tres lista



from random import randint
lista1=[]
listapar=[]
listaimpar=[]


for i in range (0,10):
    lista1.append(randint(0,50))
    if lista1[i] %2==0:
        listapar.append(lista1[i])
    else:
        listaimpar.append(lista1[i])

print (lista1)
print(listapar)
print(listaimpar)
        
