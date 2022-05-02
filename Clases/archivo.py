import csv

try:
    f = open("calificaciones (1).csv", "r")
except FileNotFoundError:
    print("El archivo no existe")
else:
    lineas = f.readlines()
    f.close()
    columnas = lineas[0].split("\t")
    seleccion = ["Apellidos" , "Nombre" , "Asistencia" , "Parcial1" , "Parcial2" , "Ordinario1" , "Ordinario2" , "Practicas" , "OrdinarioPracticas"] 
    calificaciones = []
    for linea in lineas[1:]:
        calificaciones = {}
        campos = linea.split("\t")
        for i in range(len(columnas)):
            if columnas[i] in seleccion:
                calificaciones[columnas[i]] = campos[i]
                print(calificaciones)


def leer_fichero(nombre_fichero):
    calificaciones = {}
    nombre_fichero = 'calificaciones.csv'
    with open(nombre_fichero, 'r') as fichero:
        lector = csv.DictReader(fichero)
        for fila in lector:
            calificaciones.append(fila)
    return calificaciones
    

def calcular_nota_final(calificaciones):
        for diccionario in calificaciones:
            calificacion_parcial = int(diccionario['calificacion'])
            calificacion_final = (calificacion_parcial * 0.3) + (calificacion_parcial * 0.4)
            diccionario['nota_final'] = calificacion_final
        return calificaciones


def aprobados_y_suspensos(calificaciones):
        lista_aprobados = []
        lista_suspensos = []
        for diccionario in calificaciones:
            if diccionario['nota_final'] >= 5:
                lista_aprobados.append(diccionario)
            else:
                lista_suspensos.append(diccionario)
        return lista_aprobados, lista_suspensos


