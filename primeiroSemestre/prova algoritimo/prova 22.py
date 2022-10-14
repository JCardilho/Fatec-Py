cand1 = 0
cand2 = 0
candidato3 = 0
votonulo  = 0
votobranco = 0
numeleitores = 1
cont = 0
cand4 = 0
cand5 = 0

print("-"*30)
print("1 - Candidato 1")
print("2 - Candidato 2")
print("3 - Candidato 3")
print("4 - Voto Nulo")
print("5 - Voto Branco")
print("-"*30)

while (numeleitores > 0) and (numeleitores <6):
    
    numeleitores = int(input("Digite a opção do seu candidato: "))
    print("-"*30)

    if (numeleitores > 0) and (numeleitores <6):

        cont+= 1
        
        if numeleitores == 1:
            cand1+= 1
        elif numeleitores == 2:
            cand2+=1
        elif numeleitores == 3:
            candidato3+=1
        elif numeleitores == 4:
            votonulo+= 1
        elif numeleitores == 5:
            votobranco+= 1
    else:
        print("Finalizando...")

if (votonulo != 0) or (votobranco != 0) and (cont != 0):
    porc = ((votonulo+votobranco)/cont)*100

print("-"*30)
print("Numero de votos do candidato 1:", cand1)
print("Numero de votos do candidato 2:", cand2)
print("Numero de votos do candidato 3:", candidato3)
print("Numero de votos nulo:", votonulo)
print("Numero de votos em branco:", votobranco)
print("-"*30)
print("Percentual dos votos em branco e nulos sobre o total é:", porc,"%")


   

