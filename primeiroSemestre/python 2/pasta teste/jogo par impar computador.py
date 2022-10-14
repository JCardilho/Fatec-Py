from random import randint
v = 0
P=0
I=0
while True:
    jogador= int (input("DIGA UM VALOR"))
    computador = randint (0,11)
    total = jogador + computador
    tipo = " "
    while tipo not in "P" "I":
        tipo = str (input("Par ou Impar ?P/I")). strip(). upper()[0]
    print (f"VOCÊ JOGOU {jogador} e o computador {computador}. total de {total}")
    print ("Deu Par" if total %2 == 0 else "Deu Impar")
    if tipo == "P":
        if total %2 == 0:
            print ("VOCE VENCEU")
            v +=1
        else:
            print ("VOCE PERDEU")
            break
    elif tipo == "I":
        if total % 2 ==1 :
            print ("voce venceu")
            v+=1
        else:
            print ("voce perdeu")
            break
    print ("vamos jogar novamente")
    print (f"game over ! voce venceu {v} vezez")
