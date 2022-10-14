def logicaExibe(nome, vrhora, qtdHoras, kmRodado, tp, total, totalBruto, desconto, totalDeslocamento, totalLiquido):
    print("O nome do funcionário é: %s"%nome)
    print("O valor de deslocamento é: %.2f"%totalDeslocamento)
    print("Total salário hora: %.2f"%total)
    print("Total bruto: %.2f"%totalBruto)
    print("Total desconto: %.2f"%desconto)
    print("Total liquido: %.2f"%totalLiquido)



def insere():
    print("Informe o nome do funcionário")
    nome=str(input())
    print("Informe o valor hora trabalhada")
    vrhora=float(input())
    print("Informe a qtd de horas trabalhadas")
    qtdHoras=float(input())
    print("Informe a quantidade de km rodados")
    kmRodado=float(input())
    print("Informe o tipo de contratação")
    tp=str(input())
##CHAMADA DA FUNCAO LOGICA DE NEGOCIOS COM PARAMETROS    
    logicaDeNegocios(nome, vrhora, qtdHoras, kmRodado, tp)

def logicaDeNegocios(nome, vrhora, qtdHoras, kmRodado, tp):

    total=qtdHoras * vrhora
    totalBruto=kmRodado * 0.51 + total
    totalDeslocamento = kmRodado * 0.51
    desconto = float(0.0)
    totalLiquido = float(0.0)
    if (tp=="PF"):
        desconto = totalBruto * 0.06
        totalLiquido = totalBruto - desconto

    logicaExibe(nome, vrhora, qtdHoras, kmRodado, tp, total, totalBruto, desconto, totalDeslocamento, totalLiquido) 


insere()
