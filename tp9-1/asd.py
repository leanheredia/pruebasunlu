num1 = input('ingrese algo: ')
num2 = input('ingrese otro algo: ')

if len(num1) > len(num2):
    print(f'{num1} tiene mas letras que {num2}')
else:
    print(f'{num2} tiene mas letras que {num1}')