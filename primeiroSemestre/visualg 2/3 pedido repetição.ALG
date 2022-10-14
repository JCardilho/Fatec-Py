Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
 
// Descrição   : Criar o cadastro de uma pessoa recebendo o nome, a cidade e
// a sigla do estado. Se o estado for Rio de Janeiro imprimir a mensagem
//carioca, se o estado for São Paulo imprimir a mensagem paulista, se o estado
// for Minas Gerais imprimir a mensagem mineiro, senão imprimir a mensagem
//outros estados.

// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 24/09/2021
Var
// Seção de Declarações das variáveis 

  idade, opcao,cont1,cont2:inteiro
  cont3,cont4:real
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

cont1<-0
cont2<-0
cont3<-0
cont4<-0
idade <- 0

enquanto idade >= 0 faca

         escreval("Digite a IDADE")
         escreval("-------------------------")
         leia(idade)
         
         se idade >= 0 entao
            escreval("------------------------")
            escreval("MENU DE OPÇÕES : 1-CASADA  2-SOLTEIRA  3-VIUVA  4-DIVORCIADAS ")
            escreval("------------------------")
         
            escreval("DIGITE A OPÇÃO :")
            leia (opcao)
            escreval("-------------------------")
         
            escolha opcao
            caso 1
                 cont1 <- cont1+1
            caso 2
                 cont2 <- cont2 +1
            caso 3
                 cont3 <- cont3+1
                 soma3 <- soma3+idade
            caso 4
                 cont4 <- (cont1+cont2+cont3+cont4)*0.10
            fimescolha

         senao
              escreval("Finalizando....")
              escreval("-------------------------")
              fimse

fimenquanto

se (soma3 <> 0) e (cont3 <> 0 ) então
   media3 <- soma3/cont3
fimse

         escreval ("nº de casadas são : ", cont1)
         escreval ("nº de solteiras :", cont2)
         escreval ("A média de viuvas são :", cont3)
         escreval ("A Porcentagem de divorciadas :",cont4)


fimalgoritmo



