
#Una función que reciba el fichero de calificaciones (1).txt y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.
import csv


def leer_fichero(nombre_fichero):
    lista_diccionarios = []
    with open(nombre_fichero, 'r') as fichero:
        lector = csv.DictReader(fichero)
        for fila in lector:
            lista_diccionarios.append(fila)
    return lista_diccionarios
    

def calcular_nota_final(lista_diccionarios):
        for diccionario in lista_diccionarios:
            calificacion_parcial = int(diccionario['calificacion'])
            calificacion_final = (calificacion_parcial * 0.3) + (calificacion_parcial * 0.4)
            diccionario['nota_final'] = calificacion_final
        return lista_diccionarios


def aprobados_y_suspensos(lista_diccionarios):
        lista_aprobados = []
        lista_suspensos = []
        for diccionario in lista_diccionarios:
            if diccionario['nota_final'] >= 5:
                lista_aprobados.append(diccionario)
            else:
                lista_suspensos.append(diccionario)
        return lista_aprobados, lista_suspensos
