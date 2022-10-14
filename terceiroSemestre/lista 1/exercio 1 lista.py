#01) Crie um algoritmo onde o usuário possa escolher uma unidade de medida
#distancias,capacidade  (litros),  peso  e  bytes.  Depois  peça  para  ele
#digitar  um  valor  qualquer  e aparecer na telacomo no exemplo:1 km equivale
#a:•0.625 Milhas•1000 Metros•100000 Centímetros•1000000 Milímetros.
#Ao finalperguntar se ele deseja exibir novamente.Colocar cada opção em uma
#função
def litros (valor):
    litro=valor
    mililitro=litro*1000
    centrilitro=litro*100
    decilitro=litro * 10
    print(f"{litro} litro(s)   equivale :")
    print(f"{decilitro}       decilitros")
    print(f"{centrilitro}     centrilitros")
    print(f"{mililitro}       mililitros")

def peso (valor):
    quilo=valor
    grama = quilo * 1000
    miligrama = quilo * 1000000
    micrograma = quilo * 1000000000
    print(f"{quilo} kilo(s)   equivale :")
    print(f"{grama}   gramas ")
    print(f"{miligrama}  miligramas ")
    print(f"{micrograma}  microgramas ")
    

def bytes(valor):
    byte=valor
    bits = byte * 8
    Kilobyte =byte / 2**10
    Megabyte = byte / 2**20
    Gigabyte = byte / 2**30
    print(f"{byte} bytes   equivale :")
    print(f"{bits}   bits")
    print(f"{Kilobyte}  Kilobyte (KB)")
    print(f"{Megabyte}  Megabyte (MB)")
    print(f"{Gigabyte}  Gigabyte (GB)")
    
verificador = False
while verificador == False :
    opcao= int (input("Digite 1- para litros 2- Para peso e 3- Para bytes  : "))
    if opcao >= 1 and opcao <= 3 :
            valor= int (input("Digite um valor para conversão  :  "))
    
            if opcao ==1:
                litros(valor)                

            elif opcao ==2:
                peso(valor)                

            elif opcao ==3:
                bytes(valor)

            verificador = True 

    else:
        print ("0PÇÃO INVALIDA")
        verificador = False 


