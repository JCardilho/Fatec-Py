vtCodigo=[]
vtProduto=[]
vtEstoque=[]
vtValor=[]
tamanho=int(0)

##Carrega Arquivo codigo
arquivoCodigo = open("C:\\temp\\arqCodigo.txt", "r")
##Carrega Arquivo codigo
arquivoProduto = open("C:\\temp\\arqProduto.txt", "r")

##Carrega Arquivo codigo
arquivoValor = open("C:\\temp\\arqValor.txt", "r")


##Carrega Arquivo codigo
arquivoEstoque = open("C:\\temp\\arqEstoque.txt", "r")

arquivoVenda = open("C:\\temp\\arqVenda.txt", "w")


def carregaArquivo():
    global tamanho       
    for linha in arquivoCodigo:
        vtCodigo.append(int(linha))
        tamanho = tamanho +1
    
    for linha in arquivoProduto:
        vtProduto.append(linha)


    for linha in arquivoValor:
        vtValor.append(float(linha))


    for linha in arquivoEstoque:
        vtEstoque.append(int(linha))


##Insere itens
##def fInsere():
##    for indice in range(0,tamanho):
##        vtCodigo.insert(indice, indice + 11)
##        vtProduto.insert(indice, "P"+ str(indice + 110))
##        vtValor.insert(indice, indice + 1000.50)
##        vtEstoque.insert(indice, indice + 5)

##Exibe valores
def fExibe():
    print("Código", "Produto", "Valor", "Estoque")
    for indice in range(0,tamanho):
        print(vtCodigo[indice],"    ",  vtProduto[indice], " ",vtValor[indice], "   ",vtEstoque[indice])
        ##print(vtCodigo[indice],"    ",  vtProduto[indice])


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

def fVenda():
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
        arquivoVenda.write(str(vtProduto[vtVendaIndice[indice]]))
        ##print(vtProduto[vtVendaIndice[indice]])
        ##print(vtVendaQtd[indice])
        ##print(vtValor[vtVendaIndice[indice]]*vtVendaQtd[indice])
        total=total + vtValor[vtVendaIndice[indice]]*vtVendaQtd[indice]    
        arquivoVenda.write("Total de cada item: "+str(total))
    ##print("Total de venda %.2f"%total)
    arquivoVenda.write("Total de venda "+str(total))
    arquivoVenda.close()

##fInsere()
carregaArquivo()
fExibe()
fVenda()

