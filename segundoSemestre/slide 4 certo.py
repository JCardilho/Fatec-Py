#4)Escreva uma função que receba uma string e uma lista.A função deve comparar
#a string passada como elementos da lista, também passada como parâmetro.
#Retorne verdadeiro se a string for encontrada dentro da lista, e falso em caso
#contrário
#-------------------------------------------------------- FUNÇÕES
def consulta(pesq, lista):
    if pesq in lista :
        resu=1
    else:
        resu=0

    return resu

print ("PROGRAMA PRINCIPAL")

nomes=[]
for i in range (5):
    nomes.append(input("Entre com nome: "))

print (nomes)
resp= "S"
while resp.upper () != "N":
    busca = input ("Digite um nome para busca : ")
    ret=consulta (busca,nomes)
    if ret:
        print ("nome encontrado")
    else:
        print ("nome não encontrado")

    resp= input ("Deseja continuar S/N ?")

    

    
    
    
