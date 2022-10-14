arquivo = open("C:\\temp\\arqTeste.txt","r+")

def carregaArquivoTextoApartideDe():
    arquivo.seek(10)
    print("Leitura a partir do byte 10 %s"%arquivo.tell() )
    print(arquivo.read(8))
    
def criaArquivo():
    arquivo = open("C:\\temp\\arqTeste.txt","a")
    arquivo.write("Linha01\n")
    arquivo.write("Linha02\n")
    arquivo.write("Linha03\n")
    print("Arquivo criado")
    arquivo.close()
###criaArquivo()



def criaArquivoAlteraLinhas():
    arquivo = open("C:\\temp\\arqTeste.txt","r+")
    arquivo.seek(8)
    arquivo.write(str(chr(9))+"LinhaNova")
    print("Arquivo alterado a partir do byte 8")
    arquivo.close()

##criaArquivoAlteraLinhas()
carregaArquivoTextoApartideDe()
