#. Crea un script que le solicite al usuario ingresar su edad. Verifica que el dato ingresado sea válido, teniendo en cuenta que la edad es un número entero, y el rango válido para este programa es de 18 a 60 años. El programa debe solicitar el reingreso de manera indefinida, hasta que el dato sea correcto 

edad = input('Ingresa tu edad: ')

while edad.isalpha() or (int(edad) < 18 or int(edad) > 60):
    if edad.isalpha():
        print('Debe ingresar un valor numerico.')
    else:
        print('Debe ingresar valores entre 18 y 60.')
    edad = input('Ingresa tu edad: ')


edad = int(edad)
print(f'Edad: {edad}')