def fatorial (num):
	if num == 1:
		return 1
	else:
		resultado = num * fatorial(num-1)
		return resultado


entrada = int(input("Entrada: "))
resul = fatorial(entrada)
print("O RESULTADO E: ", resul)
