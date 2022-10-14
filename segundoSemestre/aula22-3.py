# faça um programa que leia 10 numeros inteiros e armazene os numeros pares na
#lista par e os numeros impares na lisra impar imprima as tres lista



from random import randint
listaA=[]
listaB=[]
for i in range (0,10):
    listaA.append(randint(0,50))
    listaB.append (listaA[i] / 2)

listaA.sort()
listaA.reverse()
listaB.sort()

print(listaA)
print (listaB)

