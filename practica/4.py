'''
Pedir notas al usuario.

Condiciones:

Cada nota debe estar entre 0 y 10
El usuario termina ingresando -1

Al final:

Mostrar promedio de notas válidas
'''

notas = input('Ingresar notas: ')
contador = 0
suma = 0

while notas != '-1':
    while not notas.isdigit():
        print('Error. Solo admite numeros enteros.')    
        notas = input('Ingresar notas: ')
        
    notas = int(notas)
    while (notas < 0 or notas > 10):
        print('Error. Solo se admiten de 0 a 10.')
        notas = int(input('Nota agregada: '))
    
    contador +=1
    suma +=notas

    notas = input('Ingresar notas: ')
    
promedio = suma / contador
print(f'El promedio es {promedio}')