def cantidad(p):
	canti = len(p)
	return canti
	
def transformar(p):
	palabra=p.upper()
	nueva=''
	for letra in palabra:
		if letra == "Ñ":
			nueva = nueva + "N"
		else:
			nueva = nueva + letra
		
		
	return nueva
	

def main():
	palabra=input("Ingrese palabra (que contenga ñ) :")
	while "ñ" not in palabra:
		print("Palabra inválida")
		palabra=input("Ingrese palabra (que contenga ñ) :")
		
	canti = cantidad(palabra)
	print("Su palabra tiene ", canti, " letras")
	transformada = transformar(palabra)
	
	print("Su palabra transformada es ", transformada)

main()