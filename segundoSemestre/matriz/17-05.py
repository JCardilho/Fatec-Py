#1) Faça um programa que preencha uma matriz 3 x 5, e depois calcule e mostre:
#◦O maior elemento da matriz e em qual linha e coluna ele está armazenado (tem guardar os índices)
#◦A média dos números ímpares da matriz
#◦Mostre na tela todos os números primos, se houver.

from random import randint
matriz=[]
impar=[]
maior=somaimp=contimp=media=0
for l in range (3):
    linha=[]
    for c in range (5):
        linha.append(randint(1,50))
    matriz.append(linha)
for i in range(3):
    for j in range (5):
        if i==0 and j==0:
               maior =matriz[0][0]
        if matriz[i][j] > maior:
               maior=matriz[i][j]
               l=i
               c=j
        if matriz[i][j] %3==0:
            somaimp += matriz[i][j]
            contimp+=1
        num=matriz[i][j]
        cont=0
        for k in range(1,num+1):
            
            if num % k ==0 :
                cont+=1
        if cont == 2 :
            impar.append(num)

if somaimp > 0:
    media =somaimp/contimp
for p in matriz:
    print(p)
    
print (f"O maior elemento da matriz {maior}e esta na linha{l} e coluna{c}")
print (f"A média dos números ímpares da matriz é: {media:,.2f}")
print (f"Os números primos são: {impar}")
