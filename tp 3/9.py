#9. Crea un script que, sabiendo cuántos pesos argentinos tiene una persona ahorrada en su cuenta (almacenando ese monto en una variable), muestre en pantalla los montos convertidos en dólares (U$1 = $80.5), reales ($R1 = $14.1), y euros (€1 = $69.5). La salida del programa debe tener el siguiente formato: 

plata_ahorrada = float(input('Ingresa la plata ahorrada en tu cuenta: '))

pesos_usd = plata_ahorrada / 80.5
pesos_reales = plata_ahorrada / 14.1
pesos_euros = plata_ahorrada / 69.5

print('Tu plata ahorrada en dolares es:', pesos_usd, 'en reales es:', pesos_reales,'y en pesos_euros', pesos_euros)