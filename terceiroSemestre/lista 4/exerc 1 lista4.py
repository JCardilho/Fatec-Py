from random import randint 

def fcod(matriz1):
    opcao="S"
    print (matriz1)
    while opcao.upper() == "S":
        
        cod1 = int(input("digite um codigo para pesquisar o produto :")) 
        ver=False
        for i in range (0,3):                   
            if (cod1 == matriz1[i][0]):
                ver=True
                r=i
        if ver == True :        
            print ("produto cadastrado ") 
            print (f"codigo   {matriz1[r][0]}")
            print (f"produto  {matriz1[r][1]}")
            print (f" valor   {matriz1[r][2]}")
            print (f"estoque  {matriz1[r][3]}")        
        if ver == False:
            print ("produto não cadastrado ")
            
        opcao=str(input ("Deseja consultar outro produto S/N "))
        if opcao.upper =="N":
            print ("Finalizado Consulta de produto")
    

def fcompra(matriz2):
    print (matriz2)
    ver= False
    opcao="S"
    compras=[]
    cont=0
    while opcao.upper() == "S":        
        cod1 = int(input("digite um codigo para iniciar a COMPRA :"))
        for m in range (0,3):            
            if (cod1 == matriz2[m][0]):
                ver=True
                x=m
        if ver == False:
            print ("produto não cadastrado ")
        if ver == True :
            quantcom=float(input("Digite a quantidade desejada:"))
            if quantcom <= matriz2[x][3]:
                compras.append(matriz2[x])
                tot=quantcom - matriz2[x][3]
                cont+=1
                print (f"{quantcom} desejada de {matriz2[x][3]} estoque, resta {tot}")  
            else:
                print (f"Não temos  a quantidade doproduto no estoque: o saldo é {matriz2[x][3]}")
        opcao=str(input ("Deseja inserir outro produto S/N "))
    if opcao.upper() == "N":
        for w in range (cont):
            total=0
            print (f"{compras[w]}")
            total+= (compras[w][2])
        print (f"O total da compra foi {total}")
            

matriz=[] 
for i in range (3): 
    lista=[] 
    codigo= (randint(1,100))#float (input("digite codigo do produto  :")) 
    lista.append(codigo) 
    produto=str (input("Digite o nome do produto  :")) 
    lista.append(produto) 
    valor= (randint(1,100))#float (input("Digite o valor do produto :")) 
    lista.append(valor) 
    estoque=(randint(1,100))#float (input("Digite a quantidade no estoque disponivel : ")) 
    lista.append(estoque) 
    matriz.append(lista) 

o=str(input ("Deseja consultar produtos pelo codigo 'S' ou 'N' ('N'opçao para iniciar compras)  "))
if o.upper() =="S":
    fcod(matriz)
    o="N"
if o.upper() =="N":
    fcompra(matriz)
else :
    print ("Opção Invalida")
