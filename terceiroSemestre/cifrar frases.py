#cifrar frase tabela ascii

def cifra(fraser): 
    vogal=["A","E","I","O","U"] 
    consoante=["B","C", "D"," F", "G","H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X","Z"] 

    for i in range ( len (fraser)):
        if fraser[i] in vogal:  
            fraser[i]=(ord(fraser[i])+4)
            fraser[i]= (chr(fraser[i]))            

        else:
            if fraser[i] != " ":
                fraser[i]=(ord(fraser[i])-5)
                fraser[i]= (chr(fraser[i]))
            else:
                fraser[i]= " "

    fraser=" ".join(fraser)       
    print(f" Afrase cifrada é : {fraser}")     

fraser= str(input("Informe uma frase")) 

fraser=fraser.upper()
cifra(list(fraser)) #transformar em lista
print (f"Afrase original é :{fraser}")
