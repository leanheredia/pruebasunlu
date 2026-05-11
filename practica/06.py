'''
Pedir números (termina con -1).

Condiciones:

Validar que sean números

Contar:

Cuántos son pares
Cuántos son impares
'''


numero = input('Ingresa un numero: ')
pares = 0
impares = 0
contador = 0

while numero != '-1':
    while not numero.isdigit():
        print('Solo se permiten numeros enteros.')
        numero = input('Ingresa un numero: ')

    numero = int(numero)
    contador += 1
    if numero % 2 == 0:
        pares += 1
    elif numero % 2 == 1:
        impares += 1
    numero = input('Ingresa un numero: ')

print(f'Ingresaste {contador} numeros.')
print(f'{pares} de ellos fueron par.') 
print(f'{impares} de ellos fueron impares.')       