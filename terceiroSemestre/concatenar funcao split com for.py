def contarPalavras(frase):
    print (frase)
    resultado=[]
    for i in range (len (frase)):
        frase[i].split()
        resultado.append(frase[i])
    
    print (resultado)
    print (len(resultado))
    return resultado


frase = input('Informe uma frase: ')
re=contarPalavras(frase)
print (re)
