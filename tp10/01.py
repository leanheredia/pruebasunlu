'''Todas las variables y valores en Python tienen definido implícitamente un tipo. Mediante el uso de la función type(...), podemos averiguar el tipo de un dato en determinado momento del programa. Utiliza la función type para mostrar en pantalla los tipos de los siguientes valores:

'Hola mundo'
"Hola mundo"
100
'100'

Luego de haber determinado los tipos de los valores listados, responde:
¿De qué tipo son las cadenas de caracteres en Python?
¿Cuáles son las dos formas de escribir strings en Python? Investigue cuál es la diferencia entre ambas.
¿Es lo mismo que una variable tenga asignado el valor 100 a que tenga el valor ‘100’? ¿Cuál es la diferencia?'''


print(type('Hola mundo'))
print(type("Hola mundo"))
print(type(100))
print(type('100'))

'''
¿De qué tipo son las cadenas de caracteres en Python?
    Son un string

¿Cuáles son las dos formas de escribir strings en Python? Investigue cuál es la diferencia entre ambas.
    '' "", Es lo mismo en funcionalidad, pero si el texto tiene dentro comillas dobles, conviene usar comillas simples y viceversa.
¿Es lo mismo que una variable tenga asignado el valor 100 a que tenga el valor ‘100’? ¿Cuál es la diferencia?
    No, no es lo mismo. A una le estas asignando un int con valor 100, y a la otra un string con valor 100.
    
'''