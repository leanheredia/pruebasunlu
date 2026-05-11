'''
Mostrar un menú:

Saludar
Despedirse

Pedir opción al usuario.

Condiciones:

Solo se permite "1" o "2"
Si pone otra cosa → volver a pedir

Acciones:

1 → mostrar "Hola!"
2 → mostrar "Chau!"
'''


print('//MENU//')
print('1-Saludar')
print('2-Despedirse')
decision = input('Ingresa una opcion (1-2): ')

while decision != '2' and decision != '1':
    print('Error. Es 1 o 2.')
    decision = input('Ingresa una opcion (1-2): ')

if decision == '1':
    print('Hola!')
elif decision == '2':
    print('Chau!')