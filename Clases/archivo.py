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
    lista_diccionarios = []
    nombre_fichero = 'calificaciones.csv'
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
