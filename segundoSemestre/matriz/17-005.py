#2) Faça um programa que, leia uma matriz 5x2 com os números de telefones dos
#clientes, as linhas representam os clientes, as colunas representam os
#telefones. E uma lista de 5 elementos com os nomes dos clientes. Depois de
#preenchidos a lista e a matriz, deverá ser feito uma busca pelo nome do cliente
#, se o nome existir, deverá ser mostrado na tela, os telefones desse cliente.
from random import randint
nome=[]
tel=[]
pes=result=lotel=0
for l in range (5):
    nome.append(input("Digite o nome "))
    linha=[]
    for c in range (2):
        linha.append(randint(33322345,44302010))
    tel.append(linha)

for i in range (5):
    print( nome[i], tel [i])



pesq= input ("Digite um nome para pesquisa ou FIM para finalizar: ")
while pesq.upper() != "FIM" :
    achou="não"
    for j in range (5):
        if pesq in nome[j]:
            result=nome[j]
            lotel=tel[j]
            achou="sim"
    if achou == "sim":
        print (f"Oresultado da pesquisa é : {result}- {lotel}")
    if achou != "sim" :
        print ("nome não localizado ")
    pesq= input ("Digite um nome para pesquisa ou FIM para finalizar: ")
    
