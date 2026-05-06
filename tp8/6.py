edad = ''
cant_nogusto = 0
cant_recomienda = 0
edad_disguto = 0
edad_recomienda = 0
personas = 1

edad = int(input('Ingresa tu edad, persona 1: '))
while edad != 0:
    
    if (edad >= 5 and edad <= 100):
        
        gusto = input('Te gusto el helado? (Si/No): ').lower()
        recomienda = input('Recomendarias el helado (Si/No): ').lower()
       

        if gusto == 'no':
            cant_nogusto +=1
            if edad < 15:
                edad_disguto += 1
        elif recomienda == 'si':
            cant_recomienda += 1
            edad_recomienda += edad
        personas +=1
    else:
        print('Fuera de rango')
    edad = int(input(f'Ingresa tu edad, persona {personas}: '))



if cant_recomienda > 0:
    promedio = edad_recomienda / cant_recomienda
else:
    promedio = 0
print(f'Cantidad de clientes que recomendaron la heladeria: {cant_recomienda}')
print(f'Cantidad de clientes que no les gusto el helado: {cant_nogusto}')
print(f'Ojo! A {edad_disguto} menores no les gusto el helado.')
print(f'El promedio de la edad de los clientes que recomiendan la heladeria es: {promedio}')