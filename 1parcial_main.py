from funciones import *

def imprimir_menu():
    menu = """/n
    Este es el menu: 
    1) Opcion 1 -Listar todos los jugadores
    2) Opcion 2 -Por indice listar sus caracteristicas
    3) Opcion 3 -Guarda estadisticas en un CSV
    4) Opcion 4 -Buscar jugador por nombre y mostar logro
    5) Opcion 5 -Mostrar promedio de puntos por partido
    6) Opcion 6 -Ingresar nombre Y ver si es miembro del Salon de la fama
    7) Opcion 7 -Mostar jugador con el mayor porcentaje reboters totales
    8) Opcion 8 -Mostar con mayor porcentaje de tiros de campo
    9) Opcion 9 -Mostar la mayor cantidad de asistencias totales
    10) Opcion 10 -Ingresar un valor y mostrar los que promediaron mas puntso por partido
    11) Opcion 11 -Ingresar un valor y mostar los que promediaron mas rebotes por patido
    12) Opcion 12 -Ingresar un valor y mostrar los que promediaron mas asistencias por partido
    13) Opcion 13 -Mostar el jugador con mayor cantidad de robos totales
    14) Opcion 14 -Mostrar el jugador con la mayor cantidad de bloqueos totales
    15) Opcion 15 -Ingresar un valor y mostar que hayan teniado procentaje superior de tiros libres
    16) Opcion 16 -Mostar el promedio de putnor por partido excluyendo al menor cantdad de puntos por partido
    17) Opcion 17 -Mostara el jugador con la mayor cantidad de logros obtenidos
    18) Opcion 18 -Ingresar un valor y mostar los que hayan tenido procentaje de tiros libres mayor
    19) Opcion 19 -Mostar el jugador con l amayor cantidad de temporadas jugadas
    20) Opcion 20 -Ingresar un valor y mostar los jugadores ordenados por posicion
    21) Bonnus -         
    """
    return menu





menu = imprimir_menu()

while True:
    opcion = input(menu)

    match int(opcion):
        case 1:
    
           listar_todos_los_jugadores(lista_jugadores_json)
        
        case 2:
            mostrar_estadisticas_jugador(lista_jugadores_json)

        #case 3:
        #    resultado_punto3 = guardar_estadisticas_csv(jugador_seleccionado)
        #    print(resultado_punto3)

        case 4:
            buscar_jugador_por_nombre(lista_jugadores_json)

        case 5:
            calcular_promedio_puntos_por_partido(lista_jugadores_json)

        case 6:
            verificar_miembro_salon_fama(lista_jugadores_json)

        case 7:
            obtener_jugador_mayor_rebotes(lista_jugadores_json)

        case 8:
            obtener_jugador_mayor_porcentaje_tiros_campo(lista_jugadores_json)

        case 9:
            obtener_jugador_mayor_asistencias_totales(lista_jugadores_json)

        case 10:
            mostrar_jugadores_mayor_promedio_puntos(lista_jugadores_json)

        case 11:
            mostrar_jugadores_mayor_promedio_rebotes(lista_jugadores_json)

        case 12:
            mostrar_jugadores_mayor_promedio_asistencias(lista_jugadores_json)
        
        case 0:
            print("Nos vemos!")

        case _:
            print("Opcion invalida")

    input("Toque cualquier tecla para volver al menu: ")






