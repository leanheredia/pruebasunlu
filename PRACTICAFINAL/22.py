'''
Consigna 3: La empresa de criptografía "Decifralo Si Podés" debe realizar la encriptación de los nombres de jugadores del Mundial 2026. Para eso nos piden hacer dos funciones: La primera tiene que cargar los nombres y generar la lista con los nombres encriptados, la carga finaliza cuando se ingresa como nombre "FIN". La otra función debe recibir la lista encriptada y desencriptarla.
El algoritmo de encriptación es: Si el nombre tiene más de 10 letras, se deberá reemplazar cada letra por su valor ASCII correspondiente, si no, al valor ASCII de cada letra se le sumará 6. Los valores ASCII válidos para este ejercicio son el 32 (espacio) y desde el 65 al 90 (Mayúsculas) (Validar).
El valor ASCII de un carácter se obtiene con: nro_ascii=ord(letra) ejemplo ord("A") retorna 65
El carácter ASCII de un número se obtiene con ascii=chr(nro) ejemplo chr(65) retorna "A"
'''



def encriptar():
    lista_encriptados = []
    nombres = input('Ingresa el nombre del jugador: (FIN para terminar): ')
    while nombres != 'FIN':
        nombres_encriptados = []

        for letra in nombres:
            nro_ascii = ord(letra)
            if nro_ascii == 32 or (nro_ascii >= 65 and nro_ascii <= 90):
                if len(nombres) > 10:
                    nombres_encriptados.append(nro_ascii)
                else:
                    nombres_encriptados.append(nro_ascii + 6)

        lista_encriptados.append(nombres_encriptados)
        nombres = input('Ingresa el nombre del jugador: (FIN para terminar): ')

    return lista_encriptados

def desencriptar(lista_encriptados):
    lista_desencriptados = []
    for nombre in lista_encriptados:
        nombre_original = ''
        for nro_ascii in nombre:
            if len(nombre) > 10:
                asciii = nro_ascii
            else:
                asciii = nro_ascii - 6

            nombre_original += chr(asciii)

        lista_desencriptados.append(nombre_original)

    return lista_desencriptados




def main():
    lista_encriptados = encriptar()
    print(lista_encriptados)
    lista_desencriptados = desencriptar(lista_encriptados)
    print(lista_desencriptados)
main()