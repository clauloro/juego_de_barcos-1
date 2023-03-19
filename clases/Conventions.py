
"""Clase que contiene los atributos y los métodos estáticos"""
class Conventions:
    tablero_num_lineas = 10
    tablero_num_columnas = 10

    barcos_longitud = [2, 3, 3, 4, 4, 5]

    @staticmethod
    def generar_num_linea(x):
        return chr(65 + x)

    @staticmethod
    def generar_num_columna(y):
        return str(y)

    @staticmethod
    def generar_nombre_casilla(x, y):
        return generar_num_linea(x) + generar_num_columna(y)

    pass