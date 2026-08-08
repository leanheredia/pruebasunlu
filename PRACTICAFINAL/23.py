'''
La empresa "GameStats" registra todas las partidas jugadas durante un torneo de videojuegos.

La información se almacena en dos listas paralelas:

Una lista con el nombre del jugador.
Otra lista con los puntos obtenidos en esa partida.

Un mismo jugador puede aparecer varias veces porque jugó varias partidas.

Escriba una función que reciba ambas listas y retorne el nombre del jugador que obtuvo la mayor cantidad de puntos sumando todas sus partidas.
'''

def mayorpuntos(lista_nombres, lista_puntos):
    jugador_procesado = []
    for nombres in lista_nombres:
        acumulador = 0
        esta_agregado = False
        for jugador in jugador_procesado:
            if nombres == jugador:
                esta_agregado = True        
        if esta_agregado == False:
            for i in range(len(lista_nombres)):
                if nombres == lista_nombres[i]:
                    acumulador += lista_puntos[i]                
                    jugador_procesado.append(nombres)




def main():
    lista_nombres = ['Julian', 'Leandro', 'Paredes', 'Julian']
    lista_puntos = [10, 5, 3, 7]


main()