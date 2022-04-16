#función que reciba los datos del archivo calificaciones.txt y los almacene en una lista de diccionarios y retorne la lista de diccionarios 
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

#función que reciba una lista de diccionarios como la que devuelve la función anterior y añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.
def calcular_nota_final(lista_diccionarios):
    for diccionario in lista_diccionarios:
        calificacion_parcial = int(diccionario['calificacion'])
        calificacion_final = (calificacion_parcial * 0.3) + (calificacion_parcial * 0.4)
        diccionario['nota_final'] = calificacion_final
    return lista_diccionarios


