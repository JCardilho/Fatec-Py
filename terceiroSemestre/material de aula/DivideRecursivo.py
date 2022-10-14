import time
import timeit

def divideRecursivo(numero):
     divide = 0
     if numero > 0.1:
          divide=numero/2
          print("O numero %.3f"%numero , " dividido por 2 é: %.3f"%divide)
          divideRecursivo(divide)
          print(divide)
def divideNormal(numero):
     divide = 3
     while numero > 0.1:
          divide = numero/2
          print("O numero %.3f"%numero , " dividido por 2 é: %.3f"%divide)
          numero = divide

print("Informe um número")
numero = float(3)

##print("Divide normal")
##inicio = timeit.default_timer()
##divideNormal(numero)
##fim = timeit.default_timer()
##print ('duracao divide normal: %f' % (fim - inicio))


print("Divide recursivo")
inicio = timeit.default_timer()
divideRecursivo(numero)
fim = timeit.default_timer()
print ('duracao divide recursivo: %f' % (fim - inicio))
          

###Recursivo 0.457029
###duracao divide normal: 0.481598
###duracao divide normal: 0.429253

#1000000000000          
