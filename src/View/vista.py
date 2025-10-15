class Vista:
    """Clase para manejar la interfaz con el usuario"""
    
    @staticmethod
    def mostrar_menu_principal():
        print("\n" + "="*50)
        print("   SISTEMA DE TIPOS DE DATOS ABSTRACTOS (TDAs)")
        print("          Implementación con NODOS")
        print("="*50)
        print("1. TDA Archivo (Shelve + Nodos)")
        print("2. TDA Calendario (Nodos)")
        print("3. TDA Polinomio (Nodos)")
        print("4. TDA Matriz (Nodos)")
        print("0. Salir")
        print("="*50)
    
    @staticmethod
    def mostrar_menu_archivo():
        print("\n--- TDA ARCHIVO (Lista Enlazada) ---")
        print("1. Abrir archivo")
        print("2. Guardar dato")
        print("3. Leer dato")
        print("4. Modificar dato")
        print("5. Listar todos los datos")
        print("6. Cerrar archivo")
        print("0. Volver")
    
    @staticmethod
    def mostrar_menu_calendario():
        print("\n--- TDA CALENDARIO (Listas Enlazadas) ---")
        print("1. Día actual")
        print("2. Días feriados")
        print("3. Fases lunares")
        print("4. Calendario de pesca")
        print("0. Volver")
    
    @staticmethod
    def mostrar_menu_polinomio():
        print("\n--- TDA POLINOMIO (Lista Enlazada) ---")
        print("1. Crear polinomio 1")
        print("2. Crear polinomio 2")
        print("3. Sumar polinomios")
        print("4. Restar polinomios")
        print("5. Dividir polinomios")
        print("6. Eliminar término")
        print("7. Verificar término")
        print("8. Mostrar polinomios")
        print("0. Volver")
    
    @staticmethod
    def mostrar_menu_matriz():
        print("\n--- TDA MATRIZ (Lista Enlazada de Filas y Columnas) ---")
        print("1. Crear matriz A")
        print("2. Crear matriz B")
        print("3. Cargar aleatoriamente")
        print("4. Sumar matrices")
        print("5. Restar matrices")
        print("6. Multiplicar matrices")
        print("7. Mostrar matrices")
        print("0. Volver")
    
    @staticmethod
    def leer_entrada(mensaje: str) -> str:
        return input(mensaje)
    
    @staticmethod
    def mostrar_mensaje(mensaje: str):
        print(f"\n{mensaje}")
