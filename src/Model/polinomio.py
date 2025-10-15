import shelve
import calendar
import datetime
import random
from typing import List, Dict, Tuple, Optional 

from .nodos import NodoTermino

class TDAPolinomio:
    """TDA Polinomio implementado con lista enlazada de nodos"""
    
    def __init__(self):
        self.cabeza = None
    
    def insertar_termino(self, coeficiente: float, exponente: int):
        """Inserta un término en el polinomio ordenado por exponente"""
        if coeficiente == 0:
            return
        
        nuevo = NodoTermino(coeficiente, exponente)
        
        if not self.cabeza or self.cabeza.exponente < exponente:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            anterior = None
            
            while actual and actual.exponente > exponente:
                anterior = actual
                actual = actual.siguiente
            
            if actual and actual.exponente == exponente:
                actual.coeficiente += coeficiente
                if actual.coeficiente == 0:
                    if anterior:
                        anterior.siguiente = actual.siguiente
                    else:
                        self.cabeza = actual.siguiente
            else:
                nuevo.siguiente = actual
                if anterior:
                    anterior.siguiente = nuevo
                else:
                    self.cabeza = nuevo
    
    def sumar(self, otro):
        """Suma dos polinomios"""
        resultado = TDAPolinomio()
        
        actual1 = self.cabeza
        while actual1:
            resultado.insertar_termino(actual1.coeficiente, actual1.exponente)
            actual1 = actual1.siguiente
        
        actual2 = otro.cabeza
        while actual2:
            resultado.insertar_termino(actual2.coeficiente, actual2.exponente)
            actual2 = actual2.siguiente
        
        return resultado
    
    def restar(self, otro):
        """Resta dos polinomios"""
        resultado = TDAPolinomio()
        
        actual1 = self.cabeza
        while actual1:
            resultado.insertar_termino(actual1.coeficiente, actual1.exponente)
            actual1 = actual1.siguiente
        
        actual2 = otro.cabeza
        while actual2:
            resultado.insertar_termino(-actual2.coeficiente, actual2.exponente)
            actual2 = actual2.siguiente
        
        return resultado
    
    def dividir(self, otro):
        """División simple de polinomios"""
        if not otro.cabeza:
            return None, "No se puede dividir por polinomio cero"
        
        resultado = TDAPolinomio()
        
        if self.cabeza and otro.cabeza:
            coef = self.cabeza.coeficiente / otro.cabeza.coeficiente
            exp = self.cabeza.exponente - otro.cabeza.exponente
            
            if exp >= 0:
                resultado.insertar_termino(coef, exp)
            else:
                return None, "El grado del divisor es mayor que el dividendo"
        
        return resultado, "División realizada (término de mayor grado)"
    
    def eliminar_termino(self, exponente: int) -> bool:
        """Elimina un término con el exponente dado"""
        if not self.cabeza:
            return False
        
        if self.cabeza.exponente == exponente:
            self.cabeza = self.cabeza.siguiente
            return True
        
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.exponente == exponente:
                actual.siguiente = actual.siguiente.siguiente
                return True
            actual = actual.siguiente
        
        return False
    
    def existe_termino(self, exponente: int) -> bool:
        """Verifica si existe un término con el exponente dado"""
        actual = self.cabeza
        while actual:
            if actual.exponente == exponente:
                return True
            actual = actual.siguiente
        return False
    
    def __str__(self):
        """Representación en string del polinomio"""
        if not self.cabeza:
            return "0"
        
        resultado = []
        actual = self.cabeza
        primero = True
        
        while actual:
            if actual.coeficiente != 0:
                if not primero:
                    if actual.coeficiente > 0:
                        resultado.append(" + ")
                    else:
                        resultado.append(" - ")
                else:
                    if actual.coeficiente < 0:
                        resultado.append("-")
                
                coef_abs = abs(actual.coeficiente)
                
                if actual.exponente == 0:
                    resultado.append(f"{coef_abs}")
                elif actual.exponente == 1:
                    if coef_abs == 1:
                        resultado.append("x")
                    else:
                        resultado.append(f"{coef_abs}x")
                else:
                    if coef_abs == 1:
                        resultado.append(f"x^{actual.exponente}")
                    else:
                        resultado.append(f"{coef_abs}x^{actual.exponente}")
                
                primero = False
            
            actual = actual.siguiente
        
        return "".join(resultado) if resultado else "0"
