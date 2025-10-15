class TDAMatriz:
    """TDA para operaciones con matrices usando nodos"""
    
    def __init__(self, n: int = 0):
        self.n = n
        self.cabeza_filas = None
        if n > 0:
            self.crear(n)
    
    def crear(self, n: int):
        """Crea una matriz n x n usando lista enlazada de filas"""
        self.n = n
        self.cabeza_filas = None
        
        for i in range(n):
            nuevo_fila = NodoFila(i, n)
            
            if not self.cabeza_filas:
                self.cabeza_filas = nuevo_fila
            else:
                actual = self.cabeza_filas
                while actual.siguiente:
                    actual = actual.siguiente
                actual.siguiente = nuevo_fila
    
    def cargar_aleatoria(self, min_val: int = 0, max_val: int = 10):
        """Carga la matriz con valores aleatorios"""
        fila_actual = self.cabeza_filas
        
        while fila_actual:
            col_actual = fila_actual.datos
            while col_actual:
                col_actual.valor = random.randint(min_val, max_val)
                col_actual = col_actual.siguiente
            fila_actual = fila_actual.siguiente
    
    def obtener_valor(self, fila: int, col: int) -> float:
        """Obtiene el valor en posición [fila][col]"""
        fila_actual = self.cabeza_filas
        contador_fila = 0
        
        while fila_actual and contador_fila < fila:
            fila_actual = fila_actual.siguiente
            contador_fila += 1
        
        if not fila_actual:
            return 0
        
        col_actual = fila_actual.datos
        contador_col = 0
        
        while col_actual and contador_col < col:
            col_actual = col_actual.siguiente
            contador_col += 1
        
        return col_actual.valor if col_actual else 0
    
    def establecer_valor(self, fila: int, col: int, valor: float):
        """Establece el valor en posición [fila][col]"""
        fila_actual = self.cabeza_filas
        contador_fila = 0
        
        while fila_actual and contador_fila < fila:
            fila_actual = fila_actual.siguiente
            contador_fila += 1
        
        if not fila_actual:
            return
        
        col_actual = fila_actual.datos
        contador_col = 0
        
        while col_actual and contador_col < col:
            col_actual = col_actual.siguiente
            contador_col += 1
        
        if col_actual:
            col_actual.valor = valor
    
    def sumar(self, otra):
        """Suma dos matrices"""
        if self.n != otra.n:
            return None, "Las matrices deben ser del mismo tamaño"
        
        resultado = TDAMatriz(self.n)
        
        for i in range(self.n):
            for j in range(self.n):
                val = self.obtener_valor(i, j) + otra.obtener_valor(i, j)
                resultado.establecer_valor(i, j, val)
        
        return resultado, "Suma realizada correctamente"
    
    def restar(self, otra):
        """Resta dos matrices"""
        if self.n != otra.n:
            return None, "Las matrices deben ser del mismo tamaño"
        
        resultado = TDAMatriz(self.n)
        
        for i in range(self.n):
            for j in range(self.n):
                val = self.obtener_valor(i, j) - otra.obtener_valor(i, j)
                resultado.establecer_valor(i, j, val)
        
        return resultado, "Resta realizada correctamente"
    
    def multiplicar(self, otra):
        """Multiplica dos matrices"""
        if self.n != otra.n:
            return None, "Las matrices deben ser del mismo tamaño"
        
        resultado = TDAMatriz(self.n)
        
        for i in range(self.n):
            for j in range(self.n):
                suma = 0
                for k in range(self.n):
                    suma += self.obtener_valor(i, k) * otra.obtener_valor(k, j)
                resultado.establecer_valor(i, j, suma)
        
        return resultado, "Multiplicación realizada correctamente"
    
    def __str__(self):
        """Representación en string de la matriz"""
        resultado = ""
        fila_actual = self.cabeza_filas
        
        while fila_actual:
            col_actual = fila_actual.datos
            fila_str = []
            
            while col_actual:
                fila_str.append(f"{col_actual.valor:6.1f}")
                col_actual = col_actual.siguiente
            
            resultado += "  ".join(fila_str) + "\n"
            fila_actual = fila_actual.siguiente
        
        return resultado