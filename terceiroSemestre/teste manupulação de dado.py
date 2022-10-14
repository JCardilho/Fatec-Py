
#arquivo= open (".\meuarquivo.txt","a+")
#arquivo.write("Coe Lirinha, Manda video novo pra gente \n  ") # \n = pula linha
#arquivo.close()




arquivo= open (".\meuarquivo.txt","a") # w-substitui,r-leitura,a-insere no final
matriz=[]
for i in range(3):
    lista=[]
    frase= str (input("Digite uma frase  :"))
    lista.append(frase)
    matriz.append(lista)
arquivo.writelines(str(matriz)) #writelines(varias) manda para o arquivo -write(manda uma so)
arquivo.close()

with open(".\meuarquivo.txt", "r") as arquivo: # estrutura Wite abre e fecha, a variavel fica no final
    print(arquivo.readlines()) #readlines() busca o texto do arquivo

