viuvas = 0
casadas = 0
solteiras = 0
divorciadas = 0
idadesViuvas = 0
totalPessoasInformadas = 0 

idade = int(input("Insira sua idade ou 0 para sair: "))

while idade > 0:
    
    print("Informe o estado civil [1/2/3/4]")

    estado = int(input("1: Casada\n2: Solteira\n3: Viúva\n4: Divorciada \n"))

    if estado == 1:
        casadas += 1
        totalPessoasInformadas += 1
    elif estado == 2:
        solteiras += 1
        totalPessoasInformadas += 1
    elif estado == 3:
        viuvas += 1
        idadesViuvas += idade
        totalPessoasInformadas += 1
    elif estado == 4:
        divorciadas += 1
        totalPessoasInformadas += 1
    else:
        print("Valor referente ao estado civil inválido, vamos começar de novo!")
    
    idade = int(input("Insira sua idade ou 0 para sair: "))

print("O número de casados é: ", casadas)
print("O número de solteiros é: ", solteiras)

if viuvas > 0:
    print("A média das idades das pessoas viúvas é: ", (idadesViuvas/viuvas))
else:
    print("Não foram informados dados de pessoas viuvas")

if divorciadas > 0:
    print("A porcentagem de pessoas divorciadas é: ", (divorciadas/totalPessoasInformadas)*100, "%") 
else:
    print("Não foram informados dados de pessoas divorciadas")

print("Fim de execução")
