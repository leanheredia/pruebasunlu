
num1 = int(input('Ingresa el primer lado para el triangulo: '))
num2 = int(input('Ingresa el segundo lado para el triangulo: '))
num3 = int(input('Ingresa el tercer lado para el triangulo: '))

if (num1 == num2 == num3):
    print('Tu triangulo es un equilatero')
elif (num1 == num2 or num1 == num3 or num2 == num3):
    print('Tu trinangulo es isoceles')
else:
    print('Tu triangulo es escaleno')
