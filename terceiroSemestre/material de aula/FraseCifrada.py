print("Informe um nome")
frase=str("Oi mundo")
qtdCaracteres=len(frase)
print(frase)
print("A quantidade de caracteres é: %i"%qtdCaracteres)
fraseMinuscula=frase.lower()
qtdVogais=int(0)
qtdPalavras=int(1)
for qtd in range(qtdCaracteres):
    if (fraseMinuscula[qtd]=="a" or fraseMinuscula[qtd]=="e"
        or fraseMinuscula[qtd]=="i" or fraseMinuscula[qtd]=="o"
        or fraseMinuscula[qtd]=="u"):
        qtdVogais=qtdVogais+1
    elif (fraseMinuscula[qtd]==" "):    
        qtdPalavras=qtdPalavras+1     

qtdConsoantes=qtdCaracteres-(qtdPalavras+qtdVogais)+1
print("A qtd. de vogais é: %i"%qtdVogais)
print("A qtd. de palavras é: %i"%qtdPalavras)
print("A qtd. de consoantes é: %i"%qtdConsoantes)
novaFrase="123"+frase+"ABC"
print(novaFrase)
fraseCifrada=""
novaFrase=novaFrase.lower()
letraCifrada=int(0)
for qtd in range(qtdCaracteres):
    if (novaFrase[qtd]=="a" or novaFrase[qtd]=="e"
        or novaFrase[qtd]=="i" or novaFrase[qtd]=="o"
        or novaFrase[qtd]=="u"):
        letraCifrada=ord(novaFrase[qtd])+4
    else:
        letraCifrada=ord(novaFrase[qtd])-5
    fraseCifrada=fraseCifrada+chr(letraCifrada)
print("A frase cifrada é: %s"%fraseCifrada)
print("Frase original é: %s"%frase)
print("Frase com chave é: %s"%novaFrase)
