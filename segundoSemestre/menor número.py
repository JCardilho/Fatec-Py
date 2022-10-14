#1)Escreva um programa que leia um conjunto de 10 números inteiros. Calcule e mostre: 
#o menor número 
#a soma dos números pares e maiores que 10 
#a quantidade de números ímpares 
#a média dos números maiores que 20

for i in range (0,10):
    num= int (input("DIGITE UM NUMERO INTEIRO: "))

    if i == 0:
        menor = num
    if  num < menor:
        menor = num
    print (num)

    if num % 2 != 0:
print ('O MENOR NUMERO DIGITADO É :',menor)
