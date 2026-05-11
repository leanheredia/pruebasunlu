'''Ejercicio 3 — Prueba de escritorio

Decir qué muestra este código:

a = 2
b = 5
c = 0

while a <= b:
    c = c + a
    a = a + 1

print(c) Este algoritmo da como resultado 14. 
Primer vuelta: 
2 <= 5
c = 0 + 2 = 2
a = 2 + 1 = 3
print(2)

Segunda vuelta: 
3 <= 5
c = 2 + 3 = 5
a = 3 + 1 = 4
print(5)

Tercera vuelta:
4 <= 5
c = 5 + 4 = 9
a = 4 + 1 = 5
print(9)

Cuarta vuelta:
5 <= 5
c = 9 + 5 = 14
a = 5 + 1 = 6
print(14)
El resultado final es 14.

Y este otro:

x = 1
y = 3

while y >= 0:
    x = x * 2
    y = y - 1

print(x)

Primera vuelta: 
3 >= 0
x = 1 * 2 = 2
y = 3 - 1 = 2

Segunda vuelta:
2 >= 0
x = 2 * 2 = 4
y = 2 - 1 = 1

Tercera vuelta:
1 >= 0
x = 4 * 2 = 8
y = 1 - 1 = 0

Cuarta vuelta: 
0 >= 0
x = 8 * 2 = 16
y = 0 - 1 = -1
print(16)


'''
