def perimetro(base, altura):
	resu=2*base +2*altura
	return resu
'''A partir de ahora todos los programas se hace la funcion arriba, y el programa principal se hace en una función main, que es una buena practica.'''
def main(): 
	b= int(input('Ingresa un numero: '))
	h= int(input('Ingresa otro numero: '))
	peri=perimetro(b,h)
	print("El perimetro suyo es ", peri)

main()