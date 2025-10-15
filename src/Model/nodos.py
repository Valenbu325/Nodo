import shelve
import calendar
import datetime
import random
from typing import List, Dict, Tuple, Optional

# defenimos todos los nodos que se van a utilizar en los proyectos
# 1 Archivo
class NodoArchivo:
    """Nodo para almacenar información de archivos"""
    def __init__(self, clave: str, valor: any):
        self.clave = clave
        self.valor = valor
        self.siguiente = None

#Calendario 
class NodoFecha:
    """Nodo para almacenar información de fechas"""
    def __init__(self, dia: int, info: str, tipo: str):
        self.dia = dia
        self.info = info
        self.tipo = tipo
        self.siguiente = None


#polinomio

class NodoTermino:
    """Nodo para almacenar términos de polinomio"""
    def __init__(self, coeficiente: float, exponente: int):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.siguiente = None

# Matriz

class NodoFila:
    """Nodo para almacenar una fila de la matriz"""
    def __init__(self, num_fila: int, tamanio: int):
        self.num_fila = num_fila
        self.datos = self._crear_columnas(tamanio)
        self.siguiente = None
    
    def _crear_columnas(self, tamanio: int):
        """Crea lista enlazada de columnas"""
        if tamanio == 0:
            return None
        
        cabeza = NodoColumna(0, 0)
        actual = cabeza
        
        for i in range(1, tamanio):
            nuevo = NodoColumna(i, 0)
            actual.siguiente = nuevo
            actual = nuevo
        
        return cabeza


class NodoColumna:
    """Nodo para almacenar un elemento de la matriz"""
    def __init__(self, num_columna: int, valor: float):
        self.num_columna = num_columna
        self.valor = valor
        self.siguiente = None

