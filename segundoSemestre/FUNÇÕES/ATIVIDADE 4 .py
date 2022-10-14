

#Escreva uma função que receba uma string e uma lista.A função deve comparar
#a string passada como elementos da lista, também passada como parâmetro.
#Retorne verdadeiro se a string for encontrada dentro da lista, e falso em caso
#contrário
troco = []

din = float(input())

for i in range(0,11):
    
    if din != 0:
        resto = din%lista[i]
        nota = (din-resto)/lista[i]
        din = din-(nota*lista[i])
        troco.append(nota)
    else:
        troco.append(0)

troco.append(round((resto/0.01),1))

for m in range(0,12):
    troco[m] = int(troco[m])
print("NOTAS:")
for v in range(0,6):
    print("{} nota(s) de R$ {:.2f}".format(troco[v],lista[v]))
print("MOEDAS:")
for j in range(6,12):
   print("{} moeda(s) de R$ {:.2f}".format(troco[j],lista[j]))
