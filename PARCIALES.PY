a = ['Messi', 10, True, 'Diego', 'Intro', 1000, 10, 10, 10]

bandera = False

for i in a:
    if i == 'Messi':
        bandera = True

if bandera:
    print('Si que está')
else:
    print('No está')

contador = 0
for elemento in a:
    if elemento == 10:
        contador += 1
print(contador)


posicion_encontrada = -1 #porque tiene que estar vacia
for pepe in range(len(a)):
    if a[pepe] == 'Diego':
        posicion_encontrada = pepe
print(posicion_encontrada)