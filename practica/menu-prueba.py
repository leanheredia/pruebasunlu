import os


print('Sistema')
print('1_ Calcular cuadrado de un numero')
print('2_ Mostrar numeros pares hasta n')
print('3_ Mostrar cuenta regresiva')
print('4_ Salir')
decision = input('ingresa una opcion (1-4): ')

os.system('cls')
while decision != '4':

    while not (decision.isnumeric()) or (int(decision) <= 0 or int(decision) > 4):
        if not (decision.isnumeric()):
            print('Error. Solo se permiten numeros de 1-4.')
        else:
            print('Solo se permite numeros de 1-4.')
                
        decision = input('Ingresa una opcion (1-4): ')

    if decision == '1':
        numero = input('Ingresa un numero: ')
        while not (numero.isdigit()):
            print('Solo se admiten numeros.')
            numero = input('Ingresa un numero: ')
        numero = int(numero)
        cuadrado = numero ** 2
        print(f'El cuadrado de {numero}, es, {cuadrado}')
        decision = input('Ingresa una opcion (1-4): ')

    elif decision == '2':
        numero = input('Ingresa un numero: ')
        while not(numero.isdigit()):
            print('Solo se admiten numeros')
            numero = input('Ingresa un numero: ')
            
        numero = int(numero)
        while numero > 0:
            if numero % 2 == 0:
                print(numero)
            numero -= 1
        decision = input('Ingresa una opcion (1-4): ')

    elif decision == '3':
        numero = input('Ingresa un numero: ')
        while not(numero.isdigit()):
            print('Solo se admiten numeros')
            numero = input('Ingresa un numero: ')
        
        numero = int(numero)
        while numero > 0:
            print(numero)
            numero -= 1
        decision = input('Ingresa una opcion (1-4): ')
    elif decision == '4':
        print('Saliendo...')