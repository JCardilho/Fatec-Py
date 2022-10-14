#Jose luiz Cardilho e Maycom Jose de Oliveira Rodrigues 
#- Informe uma frase; 
#- Exiba quantos caracteres tem a frase; 
#- Exiba o número de vogais; 
#- Exiba o número de consoantes; 
#- Exiba o Número de Palavras; 
#- Acrescente 3 números no iníco da frase; 
#- Acrescente 3 letras no fim da frase; 
#- Exiba a frase; 
#- Faça a cifra somando mais 4 para as vogais e 
#menos 5 para os outros caracteres; 
#- Apresente a frase original seguida da frase cifrada.

def vogcom(fraser): 
    cont=0 
    cont2=0 
    vogal=["A","E","I","O","U"]    
    consoante=["B","C", "D"," F", "G","H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X","Z"] 
    caractere= len(fraser) 
    print (f"O total de caractere é : {caractere}")   
    print (fraser) 

    for i in range ( len (fraser)):
        for j in range (len(vogal)):
            if vogal[j] in fraser[i]:
                cont+=1 

    for k in range ( len (fraser)):
        for m in range ( len (consoante)): 
            if consoante[m] in fraser[k]: 
                cont2+=1  

    print(f" O total de vogal é   : {cont}")
    print(f" O total de consoante é   : {cont2}") 

def acrescentar(fraser):
    for i in range (3): 
        n1= str(input(f"Digite o {i+1} º numero ")) 
        fraser= n1 + fraser 
        n2= str(input(f"Digite o {i+1} letra "))
        fraser=  fraser + n2.upper() 
    print (fraser)     

def cifra(fraser):
    original=fraser 
    vogal=["A","E","I","O","U"]    
    consoante=["B","C", "D"," F", "G","H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X","Z"] 

    for i in range ( len (fraser)):
        if fraser[i] in vogal: 
            fraser[i]=(ord(fraser[i])+4)
            fraser[i]= (chr(fraser[i]))            

        else:
            fraser[i]=(ord(fraser[i])-5)
            fraser[i]= (chr(fraser[i]))
    fraser=" ".join(fraser)
    print (f" A frase cifrada é  : {fraser}")
     

fraser= str(input("Informe uma frase : "))
fraser=fraser.upper()     

vogcom(fraser) 
acrescentar(fraser) 
cifra(list(fraser)) #transformar em lista  
print (f" A frase original é : {fraser}")
