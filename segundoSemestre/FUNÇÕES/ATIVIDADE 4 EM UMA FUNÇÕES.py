#Escreva uma função que receba uma string e uma lista.A função deve comparar
#a string passada como elementos da lista, também passada como parâmetro.
#Retorne verdadeiro se a string for encontrada dentro da lista, e falso em caso
#contrário
#-------------------------------------------------------- FUNÇÕES
def compara():

    entrada = 0
    lista = []
    
    strin = str(input("Valor para comparar: "))
    #lista = str(input("Valores de entrada em uma linha: ")).split(" ")

    while (entrada != "NAO") and (entrada != "nao"):
        entrada = str(input("Entrada:"))
    
        if (entrada != "NAO") and (entrada != "nao"):
            lista.append(entrada)


    print(lista)
    if strin in lista:
        return True
    else:
        return False
    

#-------------------------------------------------------- PROGRAMA PRINCIPAL
    
print(compara())
