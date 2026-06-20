def encriptar_jugador(nombre):
    # 1. Validar que todo el nombre cumpla las reglas ASCII
    for letra in nombre:
        codigo = ord(letra)
        # Si NO es espacio (32) Y tampoco está entre A y Z (65-90), es inválido
        if codigo != 32 and not (65 <= codigo <= 90):
            print(f"Error: El carácter '{letra}' no es válido. Solo mayúsculas y espacios.")
            return None
            
    # 2. Si es válido, ver cuántas letras tiene para aplicar la regla
    largo = len(nombre)
    lista_ascii = []
    
    for letra in nombre:
        codigo_original = ord(letra)
        
        if largo > 10:
            # Se guarda tal cual
            lista_ascii.append(codigo_original)
        else:
            # Se guarda con el "desplazamiento" de +6
            lista_ascii.append(codigo_original + 6)
            
    return lista_ascii

def desencriptar_jugador(lista_ascii):
    largo = len(lista_ascii)
    nombre_desencriptado = ""
    
    for numero in lista_ascii:
        if largo > 10:
            # Estaba tal cual
            letra = chr(numero)
        else:
            # Estaba sumado +6, así que le restamos 6 para volver al original
            letra = chr(numero - 6)
            
        nombre_desencriptado += letra
        
    return nombre_desencriptado

# Caso 1: Nombre CORTO (<= 10 letras) -> Debería sumarle 6
nombre1 = "MESSI"  # 5 letras
encriptado1 = encriptar_jugador(nombre1)
print(f"Original: {nombre1} -> Encriptado (ASCII): {encriptado1}")
# Explicación: 'M' es 77, + 6 = 83. 'E' es 69, + 6 = 75...

# Desencriptamos
original1 = desencriptar_jugador(encriptado1)
print(f"Desencriptado: {original1}\n")


# Caso 2: Nombre LARGO (> 10 letras) -> Debería dejarlo igual
nombre2 = "DIEGO MARADONA"  # 14 letras (cuenta el espacio)
encriptado2 = encriptar_jugador(nombre2)
print(f"Original: {nombre2} -> Encriptado (ASCII): {encriptado2}")
# Explicación: Guarda los códigos reales. 'D' es 68, el espacio es 32, etc.

# Desencriptamos
original2 = desencriptar_jugador(encriptado2)
print(f"Desencriptado: {original2}")
