#include <stdio.h>
#include <stdlib.h>







int Fatorial(int n)
{ int total;    
  if (n == 1)
  {     
     printf("\n O total eh %i", n);        
     return 1;     
  }
  else
  {
     total = n * Fatorial(n-1);
     printf("\n O total eh %i", total);
     return total; 
  }

}

int main()
{
 int numero;    
 printf("\n Informe um numero qualquer ");
 scanf("%i",&numero);    
 printf("\n");
 system("pause"); 
}
///PENSAR NO RESULTADO DA FUNCAO EM CADA ETAPA
//  |CHAMADA  | NUM | FAT  | TOTAL
//  | 1º      |  5  |  24  |  120
//  | 2º      |  4  |   6  |   24
//  | 3º      |  3  |   2  |    6
//  | 4º      |  2  |   1  |    2
//  | 5º      |  1  |      |
//  |         |     |      |
//A IDÉIA É QUE O NÚMERO SEJA FATORADO ATÉ O 1
//E DEPOIS VÁ DEVOLVENDO O RESULTADO DE CADA
//FUNÇÃO MULTIPLICANDO O NUMERO PELO RESULTADO
//DE CADA FUNÇÃO.
//MAXIMO NUMERO POSSIVEL DE FATORACAO "32"
