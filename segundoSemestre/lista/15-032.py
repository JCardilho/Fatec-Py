#faça um programa que receba 10 numeros inteiros e armazene numa lista
#clacule mostre
# quantidade de numeros pares
# a soma dos numeros impares
# a quantidade de numeros entre 10 e 20 incluindo
# a média dos numero da lista
from random import randint
num =[]
contpar=0
somaimpar =0
contnum=0
for i in range (5):
    num.append (randint(1,30))#( int( input("digite um numero inteiro :")))

    if num[i] %2==0 :
        contpar+=1
    if num [i] %2 ==1 :
        somaimpar+=num[i]
    if num [i]>=10 and num [i] <= 20:
        contnum+=1
  
soma= sum(num)        
print ("Aquantidade de numeros pares",contpar)
print ("A soma dos numeros impares", somaimpar)
print ("A quantidade de numeros entre 10 e 20 :",contnum)
print ("A média dos numero da lista:", soma/5)
