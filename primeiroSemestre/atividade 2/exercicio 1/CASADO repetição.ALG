Algoritmo "semnome"
// Disciplina   : [Linguagem e L?gica de Programa??o]
// Professor   : Antonio Carlos Nicolodi
 

// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 24/09/2021
Var
// Se??o de Declara??es das vari?veis 

  casadas, solteiras, viuvas, divorciadas,idades, opcao:inteiro
  totalinformadas,idadeviuvas:real
Inicio
// Se??o de Comandos, procedimento, fun??es, operadores, etc... 

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
         escreval("DIGITE A OP??O :")
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
            escreval("Valor referente ao estado civil inv?lido, vamos come?ar de novo!")
         fimescolha


se viuvas >0 ent?o
   escreval("A m?dia das idades das pessoas vi?vas ?: ", idadeviuvas/viuvas)
   senao
   escreval("N?o foram informados dados de pessoas viuvas")
fimse
se divorciadas >0 ent?o
   escreval("A porcentagem das idades das pessoas divorciadas ?: ",  (divorciadas/totalinformadas)*100, "%")
   senao
   escreval("N?o foram informados dados de pessoas divorciadas")
fimse
escreval ("n? de casadas s?o : ", casadas)
escreval ("n? de solteiras :", solteiras)
escreval ("Digite sua idade")
leia(idades)


fimenquanto
fimalgoritmo



