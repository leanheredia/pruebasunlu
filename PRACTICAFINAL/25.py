'''La empresa "Hospital Central" registra todas las consultas médicas mediante cuatro listas paralelas:

lista_dni: DNI del paciente.
lista_especialidad: Especialidad médica en la que fue atendido.
lista_medico: Nombre del médico que realizó la consulta.
lista_minutos: Duración de la consulta (en minutos).

Cada posición representa una consulta médica.

Se pide escribir las funciones necesarias para obtener:
A)

Retornar el DNI del paciente que acumuló la mayor cantidad total de minutos en consultas.

Un mismo paciente puede aparecer muchas veces en la lista.

B)

Retornar una lista con los DNI de los pacientes que fueron atendidos por más de un médico distinto.

Por ejemplo:

Si el paciente 123 fue atendido por el Dr. Pérez y el Dr. López, debe aparecer en la lista.
Si el paciente 456 siempre fue atendido por la Dra. Gómez, no debe aparecer.
C)

Retornar la especialidad médica que realizó la mayor cantidad de consultas.
'''

def masminutos(lista_dni, lista_minutos):
    pacientes_procesados = []
    mayor_acumulador = -1
    dni_con_mayor_acumulador = -1
    for dni in lista_dni:
        esta_procesado = False
        acumulador = 0
        for pacientes in pacientes_procesados:
            if dni == pacientes:
                esta_procesado = True
        if esta_procesado == False:
            for i in range(len(lista_minutos)):           
                if dni == lista_dni[i]:
                    acumulador += lista_minutos[i]
            if acumulador > mayor_acumulador:
                mayor_acumulador = acumulador
                dni_con_mayor_acumulador = dni 
            pacientes_procesados.append(dni)

    return dni_con_mayor_acumulador


def masdeunmedico(lista_dni, lista_medico):
    pacientesmasdeun_medico = []
    for dni in lista_dni:
        medicos = []

        for i in range(len(lista_medico)):
            esta_en_medicos = False
            if dni == lista_dni[i]:
                for medico in medicos:
                    if medico == lista_medico[i]:
                        esta_en_medicos = True
                if esta_en_medicos == False:
                    medicos.append(lista_medico[i])
        if len(medicos) > 1:
            pacientesmasdeun_medico.append(dni)
    return pacientesmasdeun_medico









def main():
    lista_dni = [123, 456, 123,789]
    lista_especialidad = ['Cardiologia', 'Pediatria', 'Cardiologia', 'Clinica']
    lista_medico = ['Perez', 'Gomez', 'Lopez', 'Diaz']
    lista_minutos = [30, 20, 45, 15]
    print(masdeunmedico(lista_dni, lista_medico))
main()