'''
Una veterinaria desea registrar el peso de 8 perros.

Por cada perro:

pedir el peso en kg
validar que sea numérico y mayor a 0

El programa debe informar:

peso promedio
peso máximo y número de perro
cuántos perros pesan más de 25 kg

Si algún perro pesa más de 40 kg:

"Perro en observación veterinaria"
'''

#for para los 8 perros
#input peso y validar numero > 0 y letra
#informar peso promedio
#peso maximo (variable maxima) numero de perro (se hace con for)
#si peso > 40: observacion

peso_maximo = 0
pesan_mas_25 = 0
pesan_mas_40 = 0
num_perro = 0
suma_promedio = 0

for i in range(1,9):
    peso_perro = input(f'Ingresa el peso del perrito numero {i}: ')
    while not (peso_perro.isdigit()) or (int(peso_perro) <= 0):
        if not (peso_perro.isdigit()):
            print('Error. El peso se mide en numeros.')
        else:
            print('Error. El peso debe ser > 0')
        peso_perro = input(f'Ingresa el peso del perrito numero {i}: ')
    peso_perro = int(peso_perro)
    if peso_perro > peso_maximo:
        peso_maximo = peso_perro
        num_perro = i
    suma_promedio += peso_perro
    if peso_perro >= 25 and peso_perro < 40:
        pesan_mas_25 += 1
    elif peso_perro >= 40:
        pesan_mas_40 += 1
        

promedio = suma_promedio / 8

print(f'El peso promedio es de {promedio} kg')
print(f'El perro con el peso maximo es el perro numero {num_perro} y pesa {peso_maximo}')
print(f'Hay una cantidad de {pesan_mas_25} perros que pesan mas de 25kg')
print(f'Hay una cantidad de {pesan_mas_40} perros que estan en observacion veterinaria')
