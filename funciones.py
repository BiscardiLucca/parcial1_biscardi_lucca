import json
import re
import csv

def leer_archivo_json(ruta:str):

    with open(ruta, "r") as archivo:
        diccionario = json.load(archivo)
    return diccionario["jugadores"]

pathJson = r"C:\Users\yoluc\OneDrive\Escritorio\Programacion\Python ejercicios\Primer parcial\dt.json"

lista_jugadores_json = leer_archivo_json(pathJson)


#1
def listar_todos_los_jugadores(lista_jugadores:list[dict]):

    for jugador in lista_jugadores:
        print("{0} - {1}".format(jugador["nombre"],jugador["posicion"]))
    
resultado = listar_todos_los_jugadores(lista_jugadores_json)
print(resultado)


#2    
def mostrar_estadisticas_jugador(lista_jugadores:list[dict]):
    
    indice_jugadores = int(input("""
                                
        1 - Michael Jordan
        
        2 - Magic Johnson

        3 - Larry Bird

        4 - Charles Barkley

        5 - Scottie Pippen

        6 - David Robinson

        7 - Patrick Ewing

        8 - Karl Malone

        9 - John Stockton

        10 - Clyde Drexler

        11 - Chris Mullin

        12 - Christian Laettner

        Elija el numero que desee: """))
    
    if indice_jugadores < 1 or indice_jugadores > len(lista_jugadores):
        print("No existe ese indice")
        return
        
    jugador_seleccionado = lista_jugadores[indice_jugadores - 1]
    estadisticas = jugador_seleccionado["estadisticas"]

    print("Estadísticas de {}:".format(jugador_seleccionado["nombre"]))
    print("Temporadas jugadas: {}".format(estadisticas["temporadas"]))
    print("Puntos totales: {}".format(estadisticas["puntos_totales"]))
    print("Promedio de puntos por partido: {}".format(estadisticas["promedio_puntos_por_partido"]))
    print("Rebotes totales: {}".format(estadisticas["rebotes_totales"]))
    print("Promedio de rebotes por partido: {}".format(estadisticas["promedio_rebotes_por_partido"]))
    print("Asistencias totales: {}".format(estadisticas["asistencias_totales"]))
    print("Promedio de asistencias por partido: {}".format(estadisticas["promedio_asistencias_por_partido"]))
    print("Robos totales: {}".format(estadisticas["robos_totales"]))
    print("Bloqueos totales: {}".format(estadisticas["bloqueos_totales"]))
    print("Porcentaje de tiros de campo: {}".format(estadisticas["porcentaje_tiros_de_campo"]))
    print("Porcentaje de tiros libres: {}".format(estadisticas["porcentaje_tiros_libres"]))
    print("Porcentaje de tiros triples: {}".format(estadisticas["porcentaje_tiros_triples"]))
     
    return


#3
#No lo pude hacer


#4
def buscar_jugador_por_nombre(lista_jugadores):
    jugador_encontrado = None
    nombre_buscar = input("Ingrese el nombre del jugador a buscar: ")
    for jugador in lista_jugadores:
        if jugador["nombre"].lower() == nombre_buscar.lower():
            jugador_encontrado = jugador
            break

    if jugador_encontrado:
        print("Logros de {}:".format(jugador_encontrado["nombre"]))
        for logro in jugador_encontrado["logros"]:
            print(logro)
    else:
        print("No se encontró ningún jugador con ese nombre.")


#5
def calcular_promedio_puntos_por_partido(lista_jugadores):
    promedios_puntos = []

    for jugador in lista_jugadores:
        promedio_puntos = jugador["estadisticas"]["promedio_puntos_por_partido"]
        promedios_puntos.append((jugador["nombre"], promedio_puntos))

    promedios_puntos.sort()  # Ordenar por nombre ascendente

    for jugador, promedio in promedios_puntos:
        print("{} - Promedio de puntos por partido: {}".format(jugador, promedio))


#6
def verificar_miembro_salon_fama(lista_jugadores):
    jugador_encontrado = None
    nombre_jugador = input("Ingrese el nombre del jugador: ")
    for jugador in lista_jugadores:
        if jugador["nombre"].lower() == nombre_jugador.lower():
            jugador_encontrado = jugador
            break

    if jugador_encontrado:
        logros = jugador_encontrado["logros"]
        if "Miembro del Salon de la Fama del Baloncesto" in logros:
            print("{} es miembro del Salón de la Fama del Baloncesto.".format(jugador_encontrado["nombre"]))
        else:
            print("{} no es miembro del Salón de la Fama del Baloncesto.".format(jugador_encontrado["nombre"]))
    else:
        print("No se encontró ningún jugador con ese nombre.")


#7
def obtener_jugador_mayor_rebotes(lista_jugadores):
    jugador_mayor_rebotes = None
    max_rebotes = 0

    for jugador in lista_jugadores:
        rebotes_totales = jugador["estadisticas"]["rebotes_totales"]
        if rebotes_totales > max_rebotes:
            max_rebotes = rebotes_totales
            jugador_mayor_rebotes = jugador["nombre"]

    if jugador_mayor_rebotes:
        print("El jugador con la mayor cantidad de rebotes totales es: {}".format(jugador_mayor_rebotes))
    else:
        print("No se encontró ningún jugador.")


#8
def obtener_jugador_mayor_porcentaje_tiros_campo(lista_jugadores):
    jugador_mayor_porcentaje = None
    max_porcentaje = 0

    for jugador in lista_jugadores:
        porcentaje_tiros_campo = jugador["estadisticas"]["porcentaje_tiros_de_campo"]
        if porcentaje_tiros_campo > max_porcentaje:
            max_porcentaje = porcentaje_tiros_campo
            jugador_mayor_porcentaje = jugador["nombre"]

    if jugador_mayor_porcentaje:
        print("El jugador con el mayor porcentaje de tiros de campo es: {}".format(jugador_mayor_porcentaje))
    else:
        print("No se encontró ningún jugador.")


#9
def obtener_jugador_mayor_asistencias_totales(lista_jugadores):
    jugador_mayor_asistencias = None
    max_asistencias = 0

    for jugador in lista_jugadores:
        asistencias_totales = jugador["estadisticas"]["asistencias_totales"]
        if asistencias_totales > max_asistencias:
            max_asistencias = asistencias_totales
            jugador_mayor_asistencias = jugador["nombre"]

    if jugador_mayor_asistencias:
        print("El jugador con la mayor cantidad de asistencias totales es: {}".format(jugador_mayor_asistencias))
    else:
        print("No se encontró ningún jugador.")


#10
def mostrar_jugadores_mayor_promedio_puntos(lista_jugadores):
    jugadores_mayor_promedio = []
    valor_ingresado = float(input("Ingrese un valor de promedio de puntos: "))

    for jugador in lista_jugadores:
        promedio_puntos = jugador["estadisticas"]["promedio_puntos_por_partido"]
        if promedio_puntos > valor_ingresado:
            jugadores_mayor_promedio.append(jugador["nombre"])

    if jugadores_mayor_promedio:
        print("Los jugadores con un promedio de puntos mayor a {} son:".format(valor_ingresado))
        for jugador in jugadores_mayor_promedio:
            print(jugador)
    else:
        print("No se encontraron jugadores con un promedio de puntos mayor.")


#11
def mostrar_jugadores_mayor_promedio_rebotes(lista_jugadores):
    valor = float(input("Ingrese el valor de referencia para el promedio de rebotes por partido: "))

    jugadores_mayor_promedio = []

    for jugador in lista_jugadores:
        promedio_rebotes = jugador['estadisticas']['promedio_rebotes_por_partido']
        if promedio_rebotes > valor:
            jugadores_mayor_promedio.append(jugador['nombre'])

    if jugadores_mayor_promedio:
        print("Los jugadores con un promedio de rebotes por partido mayor a {} son:".format(valor))
        for jugador in jugadores_mayor_promedio:
            print(jugador)
    else:
        print("No hay jugadores con un promedio de rebotes por partido mayor a {}.".format(valor))


#12
def mostrar_jugadores_mayor_promedio_asistencias(lista_jugadores):
    valor = float(input("Ingrese el valor de referencia para el promedio de asistencias por partido: "))

    jugadores_mayor_promedio = []

    for jugador in lista_jugadores:
        promedio_asistencias = jugador['estadisticas']['promedio_asistencias_por_partido']
        if promedio_asistencias > valor:
            jugadores_mayor_promedio.append(jugador['nombre'])

    if jugadores_mayor_promedio:
        print("Los jugadores con un promedio de asistencias por partido mayor a {} son:".format(valor))
        for jugador in jugadores_mayor_promedio:
            print(jugador)
    else:
        print("No hay jugadores con un promedio de asistencias por partido mayor a {}.".format(valor))