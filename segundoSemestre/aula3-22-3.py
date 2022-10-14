#faça um programa que preencha uma lista com 10 nomes diferentes,uma segunda
#lista com as idades e uma terceira lista com peso. Depois permita fazer uma
#pesquisa se um determinado nome existe armazenado na lista, se existir deve
#ser impresso na tela o nome, idade, e o peso, a pesquisa deve ser feita até
#que seja digitado fim no nome a ser pesquisadona lista

from random import randint uniform
nome=[]
ida=[]
peso=[]

nome=[]
ida=[]
peso=[]

for i in range (0,3):
    nome.append(str(input("Digite seu nome :")))
    ida.append(int(input("Digite sua idade")))
    peso.append(float(input("Digite sua peso")))

pesquisa=0    
pesquisa= str (input("Digite um nome para a pesquisa"))

while pesquissa.upper!= "FIM":
    if pesquisa in nome:
        posicao=(nome.index (pesquisa))
        print (nome[(posicao)], ida [(posicao)],peso[(posicao)])
    else:
        print (pesquisa, "Não foi encontrado na lista ")


    pesquisa= str (input("Digite um nome para a pesquisa"))
