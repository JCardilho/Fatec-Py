# Faça um programa que leia uma matriz 3x3 de inteiros e retorne a linha de
#maior soma. Imprima na tela a matriz, a linha de maior soma e a soma.


from random import randint

matriz = []
somam=[]

for c in range (3):
    linha = []
    somal=0
    for l in range (3):
        numero=(randint (1,10))#int (input("digite um numero inteiro :"))
        linha.append(numero)
        somal+=numero
    matriz.append(linha)
    somam.append(somal)
somamaior= max (somam)
for i in range (3):
    if somamaior == somam [i]:
        print (somamaior)
        print (matriz)
        print (matriz[i])
        print (somamaior)
