from Clases import *

notas = int(input("Por favor seleccione el tipo de lista de los alumnos que desea consultar (1, 2 o 3): "))
if __name__ == '__main__':
    if notas == 1 :
        from Clases.archivo import leer_fichero
        lista_diccionarios = leer_fichero('Ccalificaciones (1).csv')
        print(lista_diccionarios)
    elif notas == 2 :
        from Clases.archivo import calcular_nota_final 
        lista_diccionarios = leer_fichero("calificaciones (1).csv")
        lista_diccionarios = calcular_nota_final(lista_diccionarios)
        print(lista_diccionarios)
    elif notas == 3 :
        from Clases.archivo import aprobados_y_suspensos
        lista_diccionarios = leer_fichero('calificaciones (1).csv')
        lista_diccionarios = calcular_nota_final(lista_diccionarios)
        lista_aprobados, lista_suspensos = aprobados_y_suspensos(lista_diccionarios)
        print(lista_aprobados)
        print(lista_suspensos)
