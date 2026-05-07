'''
 Implementa un algoritmo que intercambie los valores entre dos variables a y b cualesquiera. Por ejemplo, si a = 10 y b = 5, luego de ejecutar el algoritmo, la variable a debería ser igual 5, y la variable b debería ser igual a 10. 

'''
'''
a = 10
b = 5
aux = 0
print(a, b)
aux = a
a = b
b = aux

print(a, b)

'''

a = 10
b = 5
a, b = b,a 
print(a,b)