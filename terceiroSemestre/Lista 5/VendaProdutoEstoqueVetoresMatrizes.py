vtCodigo=[]
vtProduto=[]
vtEstoque=[]
vtValor=[]
matriz = []

##Insere itens
def LeituraDeArquivos():
    montagemDaMatrizPrincipal()
    tamanho = len(matriz[0])
    distribuirInformacao(tamanho)
    return tamanho

def montagemDaMatrizPrincipal():
    arquivo = open('BancoDeDados.txt','r')
    teste = arquivo.readlines()
    for i in teste:
        leitura = i.split("[")
        leitura = leitura[1].split("]")
        leitura = leitura[0].split(',')
        matriz.append(leitura)

def distribuirInformacao(tamanho):
    for indice in range(0,tamanho):
        vtCodigo.insert(indice, int(matriz[0][indice]))
        vtProduto.insert(indice, str(matriz[1][indice]))
        vtValor.insert(indice, float(matriz[2][indice]))
        vtEstoque.insert(indice, int(matriz[3][indice]))

##Exibe valores
def fExibe(tamanho):
    print("-"*67)
    print("{:^7} {:^20} {:^20} {:^20}".format('Código', 'Produto','Valor','Estoque')) # "^" CENTRALIZA
    for indice in range(0,tamanho):
        print("{:^7} {:^20} {:^20} {:^20}".format(vtCodigo[indice],vtProduto[indice],vtValor[indice],vtEstoque[indice]))
    print("-"*67)


def fBuscaCodigoProduto(codigo,tamanho):     
    for indice in range(0,tamanho):
        if (codigo == vtCodigo[indice]):
            print("-"*67)
            print("Código encontrado para o produto: ", vtCodigo[indice])
            print("Nome do produto encontrado para o produto: ", vtProduto[indice])
            print("Valor do produto encontrado para o produto: ", vtValor[indice])
            print("Estoque do produto encontrado para o produto: ", vtEstoque[indice])
            print("-"*67)

            return indice
    return -1

def fVerificaEstoque(qtd, indice):
    if (qtd> vtEstoque[indice]):
        print("Não temos esta quantidade em estoque")
        return -1
    else:
        vtEstoque[indice]=vtEstoque[indice] - qtd
        return indice

def fVenda(tamanho):
    vtVendaCodigo=[]
    vtVendaQtd=[]
    vtVendaIndice=[]
    vtIdVenda=[]
    idVenda=int(0)
    resp="S"
    while (resp.upper()=="S"):
        print("Usuário querido, informe um código para busca")
        codigo = int(input())
        indice=fBuscaCodigoProduto(codigo,tamanho)
        if (indice>-1):
            print("Informe a quantidade que deseja comprar")
            qtd=int(input())
            indice = fVerificaEstoque(qtd, indice)
            fExibe(tamanho)
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
        print("-"*67)    

    total=float(0)
    print("{:^20} {:^10} {:^20} ".format('Produto','Quantidade','Valor do Produto'))
    for indice in range(0,idVenda):
        print("{:^20}{:^10}{:^20}".format(vtProduto[vtVendaIndice[indice]],vtVendaQtd[indice],vtValor[vtVendaIndice[indice]]*vtVendaQtd[indice]))
        total=total + vtValor[vtVendaIndice[indice]]*vtVendaQtd[indice]    
    print("-"*67) 
    print("Total de venda %.2f"%total)
    print("-"*67) 

    if (len(vtVendaCodigo) > 0):
        arquivo = open('./Vendas.txt', 'a')
        arquivo.write("\n"+str("PRODUTO | QUANTIDADE | VALOR \n"))
        for indice in range(0,idVenda):
            arquivo.write(str(vtProduto[vtVendaIndice[indice]])+" ")
            arquivo.write(str(vtVendaQtd[indice])+" ")
            arquivo.write(str(vtValor[vtVendaIndice[indice]]*vtVendaQtd[indice])+" ")
            arquivo.write(str('\n'))
        
        arquivo.write("Valor Total: "+str(total)+"\n")


tamanho = LeituraDeArquivos()
fExibe(tamanho)
fVenda(tamanho)

