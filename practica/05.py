numeros = input('Ingresa un numero: ')
suma = 0
contador = 0
while numeros != '0':
    while not numeros.isdigit():
        print('Error. Los numeros deben ser enteros.')
        numeros = input('Ingresa un numero: ')
        
    numeros = int(numeros)
    contador +=1
    suma += numeros
    numeros = input('Ingresa un numero: ')
    
print(f'Usted ingreso {contador} numeros.')
print(f'La suma total de ellos es {suma}')
