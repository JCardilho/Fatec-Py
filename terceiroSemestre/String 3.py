listaEntrada = []
matriz = []

def separar():
    for i in range(0,4):
        transf = []
        transf = list(listaEntrada[i])
        transf.insert(2,"-")
        matriz.append(transf)
        
for i in range(0,4):
    entrada = str(input("Digite uma palavra: "))
    listaEntrada.append(entrada)
    
separar()

for i in range(0,4):
    print(f"{matriz[i][0]}{matriz[i][1]}{matriz[i][2]}{matriz[i][3]}{matriz[i][4]}")

