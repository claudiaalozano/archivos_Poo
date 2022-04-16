
def leer_archivo(nombre_archivo):
    lista_diccionarios = []
    archivo = open(nombre_archivo, 'r')
    for linea in archivo:
        diccionario = {}
        linea = linea.strip()
        linea = linea.split(',')
        diccionario['nombre'] = linea[0]
        diccionario['calificacion'] = linea[1]
        lista_diccionarios.append(diccionario)
    archivo.close()
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
