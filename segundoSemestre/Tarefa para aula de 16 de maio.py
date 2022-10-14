#Faça um programa que preencha uma matriz 5 x 4. A primeira coluna dessa
#matriz deve armazenar os nomes dos alunos, as colunas restantes devem
#armazenar as notas de cada aluno.
#Calcule a média de cada aluno e armazene em uma lista.
#Depois imprima um relatório com o nome do aluno e a média.

from random import randint

matriz=[]
linha=[]
mediatotal=[]
for l in range (5):
    nomes= str(input("Digite o nome do aluno : "))
    linha.append (nomes)
    for d in range (3):
        nota= (randint(1,10))
        linha.append (nota)
    matriz.append (linha)
    linha=[]
mediatotal=[]
for i in range (5):
    media=0    
    for j in range (1,4):
        media+=  (matriz[i][j])
    media= media/3
    mediatotal.append(media)
print ("-"*40)
print (matriz)
print (mediatotal)
print ("-"*40)
for i in range (5):
    print (f" O aluno : {matriz[i][0]}     finalizou com a media  : {mediatotal[i]:,.2f}")
    
    
    
