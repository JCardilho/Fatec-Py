#3) Faça um programa que preencha uma matriz 4 x 4. A primeira coluna dessa matriz deve
#armazenar os nomes dos vendedores, as colunas restantes devem armazenar as vendas.
#Calcule a média de venda de cada vendedor e armazene em uma lista. Depois imprima um
#relatório com o nome do vendedor e a média.
#E calcule qual foi o total vendido por todos vendedores no trimestre e a maior venda


from random import randint
matriz=[]
impar=[]
totalvend=[]

todos=0
for l in range (4):
    linha=[]
    linha.append(str(input("digite o nome do vendedor")))
    for c in range (3):
        linha.append(randint(100,1000))
    matriz.append(linha)
for i in range(4):
    somavend=0
    for j in range (1,4):
        somavend+=matriz[i][j]
        todos+=somavend
    totalvend.append(somavend/3)
    maiortri= totalvend[0]
    if somavend > maiortri:
        maiortri= somavend
        loc=i
        loc1=somavend
for m in range (4):        
    print (f"vendedor :  {matriz[m]} com a média : {totalvend[m]:,.2f}")
print (f" o total vendido por todos vendedores no trimestre é: {todos}")
print (f" a Maior venda foi do vendedor : {matriz[loc]} com :{loc1}")
