matriz = []

def separar(entrada):
    lista = []
    for i in range (0,4):
        lista.append(entrada[i])
    lista.insert(2,"-")
    matriz.append(lista)

for i in range(0,4):
    entrada = str(input("Digite uma palavra: "))
    separar(entrada)
    
for i in range(0,4):
    # print(matriz[i][0]+matriz[i][1]+matriz[i][2]+matriz[i][3]+matriz[i][4])
    print(f"{matriz[i][0]}{matriz[i][1]}{matriz[i][2]}{matriz[i][3]}{matriz[i][4]}")
