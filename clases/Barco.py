from clases import Conventions
from clases import Case
from itertools import product, repeat
from random import choice

class Barco:
    
    instances = []
    casillas_ocupadas = set()
    # performance / legibilidad:
    num_lineas = Conventions.tablero_num_lineas
    num_columnas = Conventions.tablero_num_columnas
    num2l = Conventions.generar_num_linea
    num2c = Conventions.generar_num_columna
    
    def __init__(self, longitud):
        self.longitud = longitud
        self.orientacion = choice(Conventions.ORIENTACIONES)
        self.tocado = False
        self.hundido = False
    
    def horizontal(self):
        if self.orientacion == Conventions.HORIZONTAL:
            rang = choice(range(self.num_lineas))
            primero = choice(range(self.num_columnas + 1 - Conventions.LONGITUDES_BARCOS))
            letra = self.num2l(rang)
            cifras = [self.num2c(x) for x in range(primero, primero + Conventions.LONGITUDES_BARCOS)]
            self.casillas = {Case.instances[l + c]
                                 for l, c in product(repeat(letra, Conventions.LONGITUDES_BARCOS), cifras)}
        else:
            rang = choice(range(self.num_columnas))
            primero = choice(range(self.num_lineas + 1 - Conventions.LONGITUDES_BARCOS))
            cifra = self.num2c(rang)
            letras = [self.num2l(x) for x in range(primero, primero + Conventions.LONGITUDES_BARCOS)]
    
            # Crear el barco
            self.casillas = {Case.instances[l + c]
                for l, c in product(letras, repeat(cifra, Conventions.LONGITUDES_BARCOS))}
        return self.casillas
    
    def instanciar(self):
        for existente in self.instances:
            if self.casillas.intersection(existente.casillas):
                # break relativo al "for existente in barcos:"
                break
            else:
                # Agregar el barco en el contenedor de barcos
                self.instances.append(self)
                # Informar la casilla que contiene un barco.
                for casilla in self.casillas:
                    casilla.contiene_barco = True
                # Agregar estas casillas a las casillas ocupadas :
                self.casillas_ocupadas.update(self.casillas)
                # break relativo al "for existente in barcos:"
                break
        else:
            # break relativo al "while True:"
            return
        
    
    def generar_barcos(self):
        while True:
            self.longitud = choice(Conventions.barcos_longitud)
            self.orientacion = choice(Conventions.ORIENTACIONES)
            self.tocado = False
            self.hundido = False
            self.horizontal()
            self.instanciar




        