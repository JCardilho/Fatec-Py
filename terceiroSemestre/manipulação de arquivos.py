vtCodigo=[]
vtProduto=[]
vtEstoque=[]
vtValor=[]
tamanho=int(5)

    
##Insere itens
def fInsere(arq):
    for indice in range(0,tamanho):
        vtCodigo.insert(indice, indice + 11)
        vtProduto.insert(indice, "P"+ str(indice + 110))
        vtValor.insert(indice, indice + 1000.50)
        vtEstoque.insert(indice, indice + 5)
    arq.write("Código do Produto "+str(vtCodigo))
    arq.write(" Produto: "+str(vtProduto))
    arq.write(" Valor em R$: "+str(vtValor))
    arq.write(" Estoque "+str(vtEstoque))
    


##Exibe valores
def fExibe():
    print("Código", "Produto", "Valor", "Estoque")
    for indice in range(0,tamanho):
        print(vtCodigo[indice],"    ",  vtProduto[indice], " ",vtValor[indice], "   ",vtEstoque[indice])


def fBuscaCodigoProduto(codigo):        
    for indice in range(0,tamanho):
        if (codigo== vtCodigo[indice]):
           print("Código encontrado para o produto", vtCodigo[indice])
           print("Nome do produto encontrado para o produto", vtProduto[indice])
           print("Valor do produto encontrado para o produto", vtValor[indice])
           print("Estoque do produto encontrado para o produto", vtEstoque[indice])
           return indice
    return -1

def fVerificaEstoque(qtd, indice):
    if (qtd> vtEstoque[indice]):
        print("Não temos esta quantidade em estoque")
        return -1
    else:
        vtEstoque[indice]=vtEstoque[indice] - qtd
        return indice

def fVenda(arq):
    vtVendaCodigo=[]
    vtVendaQtd=[]
    vtVendaIndice=[]
    vtIdVenda=[]
    idVenda=int(0)
    resp="S"
    while (resp.upper()=="S"):
        print("Usuário querido, informe um código para busca")
        codigo = int(input())
        indice=fBuscaCodigoProduto(codigo)
        if (indice>-1):
            print("Informe a quantidade que deseja comprar")
            qtd=int(input())
            indice = fVerificaEstoque(qtd, indice)
            fExibe()
            if (indice>-1):
                vtVendaCodigo.append(codigo)
                vtVendaQtd.append(qtd)
                vtVendaIndice.append(indice)
                vtIdVenda.append(idVenda)
                idVenda=idVenda+1
        else:
            print("Código de produto não encontrado")
        print("Deseja vender outro produto ['S','N'] ? ")
        resp=str(input())

    total=float(0)
    for indice in range(0,idVenda):
        print(vtProduto[vtVendaIndice[indice]])
        print(vtVendaQtd[indice])
        print(vtValor[vtVendaIndice[indice]]*vtVendaQtd[indice])
        total=total + vtValor[vtVendaIndice[indice]]*vtVendaQtd[indice]    
    
    print("Total de venda %.2f"%total)
    arq.write(str(chr(38))+" Produtos: "+str(vtProduto[vtVendaIndice[indice]]))
    arq.write(" Quantidade: "+str(vtVendaQtd[indice]))
    arq.write(" Total: \n"+str(total))
    arq.close()
    
   




arq=open("D:\\ssd\\FATEC\\3 semestre\\estrutura de dados\\todos codigos python\\open.txt","w",encoding="utf-8")
fInsere(arq)        
fExibe()
fVenda(arq)

