Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 03/12/2021
Var
cand1, cand2, candidato3, votonulo, votobranco, numeleitores : inteiro
cont, cand4, cand5 : inteiro
porc : real

Inicio

cand1 <- 0
cand2 <-0
candidato3 <- 0
votonulo <- 0
votobranco <- 0
numeleitores <- 1
cont <- 0
cand4 <- 0
cand5 <- 0

escreval("--------------------------------------")
escreval("1 - Candidato 1")
escreval("2 - Candidato 2")
escreval("3 - Candidato 3")
escreval("4 - Voto Nulo")
escreval("5 - Voto Branco")
escreval("--------------------------------------")

enquanto (numeleitores > 0) e (numeleitores <6) faça

    escreva("Digite a opção do seu candidato: ")
    leia(numeleitores)
    escreval("--------------------------------------")

    se (numeleitores > 0) e (numeleitores <6) então

        cont <- cont + 1

        escolha numeleitores
        caso 1
             cand1 <- cand1 + 1
        caso 2
            cand2 <- cand2 + 1
        caso 3
            candidato3 <- candidato3 + 1
        caso 4
            votonulo <- votonulo + 1
        caso 5
            votobranco <- votobranco + 1
        fimescolha

    senão
        escreval("Finalizando...")
    fimse
    fimenquanto
se (votonulo <> 0) ou (votobranco <> 0) e (cont <> 0) então
    porc <- ((votonulo+votobranco)/cont)*100
fimse

escreval("--------------------------------------")
escreval("Numero de votos do candidato 1:", cand1)
escreval("Numero de votos do candidato 2:", cand2)
escreval("Numero de votos do candidato 3:", candidato3)
escreval("Numero de votos nulo:", votonulo)
escreval("Numero de votos em branco:", votobranco)
escreval("--------------------------------------")
escreval("Percentual dos votos em branco e nulos sobre o total é:", porc,"%")

Fimalgoritmo
