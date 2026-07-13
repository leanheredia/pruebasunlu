'''
Ejercicio 2 - Alumnos presentes

Una escuela tiene:

inscriptos = ["ANA","JUAN","PEDRO","LUCAS"]
presentes = ["JUAN","LUCAS"]

Crear una función que genere una lista con los alumnos ausentes.

Resultado:

["ANA","PEDRO"]
'''


def alumnos_ausentes(inscriptos, presentes):
    lista_ausentes = []
    
    for alumnos in inscriptos:
        encontrado = False
        for alumnos2 in presentes:
            if alumnos2 == alumnos:
                encontrado = True
        if encontrado == False:
            lista_ausentes.append(alumnos)

    return lista_ausentes


def main():
    inscriptos = ['Ana', 'Juan', 'Pedro', 'Lucas']
    presentes = ['Juan', 'Lucas']
    print(alumnos_ausentes(inscriptos, presentes))


main()