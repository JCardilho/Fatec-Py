##Na função ele pegou o número que o usuário digitou
##na variavel númeroinicial e copiou para a variável número
def fatorial(numero):
     ##se a varíavel número for igual a 1 ele entre neste if
     if (numero==1):
          ##escreve na tela o número "1", pois ele entrou no if
          print("O total é: %i"%numero)
          ##retorna o número 1
          return 1
     ##se o número não for 1 a instrução vai entre nesta parte do código
     else:
          ##Lembrando que o código é executado da direita para a esquerda
          ##Vai chamar a função fatorial novamente (esta mesma função)
          ##Passando o valor da variável número menos 1       
          total = numero * fatorial(numero-1)
          ##A multiplicação pela variável número dentro do "else"
          ##só vai ocorrer quando houver resultado da função
          print("O total é: %i"%total)
          return total

##Linha que aparece na tela para dizer o que o usuario tem que fazer          
print("Informe um número para verificar o fatorial")
##Linha que espera o usuario digitar o valor e guarda na variavel
##numeroinicial
numeroInicial = int(input())
##Chama a função fatorial, passando como parametro o valor que o
##usuário digitou
fatorial(numeroInicial)
