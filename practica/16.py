'''
Ejercicio 1 — Control de stock y validaciones

Una distribuidora necesita registrar productos vendidos.

Se debe ingresar:

Código de producto
Mes de venta
Cantidad vendida

La carga finaliza cuando el código de producto sea 0.

Condiciones
Validar que el mes sea numérico y esté entre 1 y 12.
Validar que la cantidad vendida sea mayor a 0.
Contar cuántos errores cometió el operador.
Informar:
Total vendido.
Mes con mayor cantidad de ventas.
Cantidad de errores cometidos.

'''
errores = 0
total_vendido = 0
mes_con_mas_ventas = 0
mas_cantidad = 0
print('**\Control de stock de empresa/**')
print()
codigo_producto = input('Ingresa el codigo del producto: ')



while not (codigo_producto.isdigit()):
    print('Error. El codigo deben ser digitos')
    errores += 1
    codigo_producto = input('Ingresa el codigo del producto: ')
codigo_producto = int(codigo_producto)

while codigo_producto != 0:

    mes_venta = input('Ingresa el mes de venta: ')
    while not (mes_venta.isdigit()) or (int(mes_venta) < 1 or int(mes_venta) > 12):
        errores += 1
        if not (mes_venta.isdigit()):
            print('Error. Solo se permiten los meses en numeros.')    
        else:
            print('Error. Los meses del año son del 1 (Enero) al 12 (Diciembre)')
        mes_venta = input('Ingresa el mes de venta: ')
    mes_venta = int(mes_venta)


    cantidad_vendida = input('Ingresa la cantidad vendida del producto: ')
    while not(cantidad_vendida.isdigit()) or (int(cantidad_vendida) <= 0):
        errores += 1
        if not(cantidad_vendida.isdigit()):
            print('Error. La cantidad vendida deben ser digitos')
        else:
            print('Error. La cantidad vendida debe ser mayor a 0.')
        cantidad_vendida = input('Ingresa la cantidad vendida del producto: ')
    cantidad_vendida = int(cantidad_vendida)
    total_vendido += cantidad_vendida

    if cantidad_vendida > mas_cantidad:
        mas_cantidad = cantidad_vendida
        mes_con_mas_ventas = mes_venta

    codigo_producto = int(input('Ingresa el codigo del producto: '))


print(f'El total vendido es de {total_vendido}')
print(f'El mes con mayor ventas es {mes_con_mas_ventas}')
print(f'La cantidad de errores cometidos fueron de {errores}')