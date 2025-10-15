class TDAArchivo:
    """TDA para manejo de archivos usando nodos y shelve"""
    
    def __init__(self):
        self.archivo_actual = None
        self.cabeza = None
    
    def abrir(self, ruta: str):
        """Abre un archivo shelve y carga datos a lista enlazada"""
        try:
            self.archivo_actual = shelve.open(ruta)
            self.cabeza = None
            for clave in self.archivo_actual.keys():
                self._insertar_nodo(clave, self.archivo_actual[clave])
            return True, "Archivo abierto correctamente"
        except Exception as e:
            return False, f"Error al abrir archivo: {str(e)}"
    
    def _insertar_nodo(self, clave: str, valor: any):
        """Inserta un nodo en la lista enlazada"""
        nuevo = NodoArchivo(clave, valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
    
    def cerrar(self):
        """Cierra el archivo actual"""
        if self.archivo_actual:
            self.archivo_actual.close()
            self.archivo_actual = None
            self.cabeza = None
            return True, "Archivo cerrado correctamente"
        return False, "No hay archivo abierto"
    
    def leer(self, clave: str):
        """Lee un dato buscando en la lista enlazada"""
        if not self.cabeza:
            return None, "No hay datos en memoria"
        
        actual = self.cabeza
        while actual:
            if actual.clave == clave:
                return actual.valor, "Lectura exitosa"
            actual = actual.siguiente
        
        return None, "Clave no encontrada"
    
    def guardar(self, valor: any, clave: str):
        """Guarda un dato en la lista enlazada y en shelve"""
        if not self.archivo_actual:
            return False, "No hay archivo abierto"
        
        try:
            self.archivo_actual[clave] = valor
            self.archivo_actual.sync()
            self._insertar_nodo(clave, valor)
            return True, "Dato guardado correctamente"
        except Exception as e:
            return False, f"Error al guardar: {str(e)}"
    
    def modificar(self, clave: str, valor: any):
        """Modifica un dato en la lista enlazada y en shelve"""
        if not self.archivo_actual:
            return False, "No hay archivo abierto"
        
        actual = self.cabeza
        while actual:
            if actual.clave == clave:
                actual.valor = valor
                self.archivo_actual[clave] = valor
                self.archivo_actual.sync()
                return True, "Dato modificado correctamente"
            actual = actual.siguiente
        
        return False, "Clave no existe"
    
    def listar_datos(self):
        """Lista todos los datos almacenados"""
        datos = []
        actual = self.cabeza
        while actual:
            datos.append(f"{actual.clave}: {actual.valor}")
            actual = actual.siguiente
        return datos