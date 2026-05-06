num1 = input('Ingresa el primer numero entero: ')
num2 = input('Ingresa el segundo numero entero: ')



while num1.isalpha() and num2.isalpha():
    print('Los numeros deben ser un numero entero')
    num1 = input('Ingresa el primer numero entero: ')
    num2 = input('Ingresa el segundo numero entero: ')

if int(num1) > int(num2):
    potencia = int(num1) ** int(num2)
    print('La potencia es: ', potencia)
elif num1 < num2:
    potencia = int(num2) ** int(num1)
    print('La potencia es: ', potencia)