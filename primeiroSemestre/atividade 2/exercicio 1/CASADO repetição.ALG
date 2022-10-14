Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
 

// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 24/09/2021
Var
// Seção de Declarações das variáveis 

  casadas, solteiras, viuvas, divorciadas,idades, opcao:inteiro
  totalinformadas,idadeviuvas:real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

casadas <-0
solteiras <-0
viuvas <-0
divorciadas <-0
totalinformadas <-0
idadeviuvas <-0
idades<-1
escreval ("Digite sua idade")
leia(idades)
enquanto idades > 0 faca
         escreval("INFORME O ESTADO CIVIL[1-Casadas,2-Solteiras,3-Viuvas,4-Divorciadas")
         escreval("DIGITE A OPÇÃO :")
            leia (opcao)
            
         escolha opcao
            caso 1
                 casadas <- casadas+1
                 totalinformadas<- totalinformadas+1
            caso 2
                 solteiras <- solteiras +1
                 totalinformadas<- totalinformadas+1
            caso 3
                 viuvas <-viuvas+1
                 totalinformadas<- totalinformadas+1
                 idadeviuvas<- idadeviuvas+idades
            caso 4
                divorciadas <-  divorciadas+1
                totalinformadas<- totalinformadas+1

            outrocaso
            escreval("Valor referente ao estado civil inválido, vamos começar de novo!")
         fimescolha


se viuvas >0 então
   escreval("A média das idades das pessoas viúvas é: ", idadeviuvas/viuvas)
   senao
   escreval("Não foram informados dados de pessoas viuvas")
fimse
se divorciadas >0 então
   escreval("A porcentagem das idades das pessoas divorciadas é: ",  (divorciadas/totalinformadas)*100, "%")
   senao
   escreval("Não foram informados dados de pessoas divorciadas")
fimse
escreval ("nº de casadas são : ", casadas)
escreval ("nº de solteiras :", solteiras)
escreval ("Digite sua idade")
leia(idades)


fimenquanto
fimalgoritmo



