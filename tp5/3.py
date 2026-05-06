# 3.  Crea un script que le solicite al usuario ingresar tres números y muestre por pantalla el número máximo y mínimo.

num1 = int(input('Ingresa el primer numero: '))
num2 = int(input('Ingresa el segundo numero: '))
num3 = int(input('Ingresa el tercero numero: '))

if num1 > num2 and num1 > num3:
    print(f'El numero {num1} es el mayor.')
elif num2 > num3:
        print(f'El numero {num2} es el mayor.')
else:
    print(f'El numero {num3} es el mayor.')

# menor

if num1 < num2 and num1 < num3:
    print(f'El numero {num1} es el menor.')
elif num2 < num3:
        print(f'El numero {num2} es el menor.')
else:
    print(f'El numero {num3} es el menor.')
