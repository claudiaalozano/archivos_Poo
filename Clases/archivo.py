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
        for linea in lector:
            nombre_fichero.append(calificaciones)
    return calificaciones
    

def calcular_nota_final(calificaciones):
        for diccionario in calificaciones:
            calificacion_parcial = int(diccionario['calificacion'])
            calificacion_final = ((("Parcial1" + "Parlial2")/2) * 0.3) + ("Ordinario1" * 0.4)
            diccionario['nota_final'] = calificacion_final
        return calificaciones


def aprobados_y_suspensos(calificaciones):
        lista_aprobados = []
        lista_suspensos = []
        for diccionario in calificaciones:
            calificacion_final = ((("Parcial1" + "Parlial2")/2) * 0.3) + ("Ordinario1" * 0.4)
            if calificacion_final >= 5:
                lista_aprobados.append(calificaciones)
            else:
                lista_suspensos.append(calificaciones)
        return lista_aprobados, lista_suspensos

