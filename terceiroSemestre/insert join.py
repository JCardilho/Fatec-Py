matriz = []
matriz1=[]
vogal=["A","E","I","O","U"]
def separar(entrada):
    lista = []
    for i in range(len(entrada)):
        lista.append(entrada[i])
    lista.insert(2,"-")
    matriz.append(lista)

def colovogal(entrada):
    
    entrada =entrada.upper()
    for i in range(len(entrada)):
        lista1=[]
        if entrada[i] not in vogal:
            for j in range (5):
                re= entrada[i] + vogal[j]
                lista1.append(re)
            matriz1.append(lista1)
     
for i in range(0,4):
    entrada = str(input("Digite uma palavra com 4 letras: "))
    separar(entrada)
    colovogal(entrada)
for i in range(0,4):
    matriz[i] = " ".join(matriz[i])
    print(matriz[i])
for k in matriz1:
    print(k)