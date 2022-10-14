#faça um programa para calcular o imc de 5 pessoas
# crie uma lista para armazenar os nomes uma segunda para pesos e uma terceira lista para armazenar
#a alturas
# calcule o IMC de cada pessoa e imprima na tela um relatorio com o nome e
#o IMC de cada pessoa
# IMC = peso / (altura * altura )

nome= []
peso=[]
alt=[]
imc=[]
for i in range (5):
    nome.append (str(input("Digite o seu nome :")))
    peso.append (float(input("Digite o seu peso :")))
    alt.append (float(input("Digite a sua altura:")))
    imc.append(peso[i] / (alt[i] * alt[i]))
for i in range (len(nome)):
    print(nome[i],peso [i],alt [i],imc[i]) 
