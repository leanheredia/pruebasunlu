def misterio(lista):
    resultado = []

    for i in range(len(lista)):
        contador = 0

        for j in range(len(lista)):
            if lista[i] == lista[j]:
                contador += 1

        if contador == 1:
            resultado.append(lista[i])

    return resultado


def main():
    datos = [5, 2, 5, 8, 3, 2, 7, 8, 1]
    print(misterio(datos))

main()