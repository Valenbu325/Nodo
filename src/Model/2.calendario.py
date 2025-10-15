class TDACalendario:
    """TDA para manejo del calendario con nodos"""
    
    def __init__(self):
        self.fecha_actual = datetime.date.today()
        self.mes = self.fecha_actual.month
        self.anio = self.fecha_actual.year
        self.cabeza_feriados = None
        self.cabeza_fases = None
        self.cabeza_pesca = None
        self._inicializar_listas()
    
    def _inicializar_listas(self):
        """Inicializa las listas enlazadas con información del mes"""
        self._cargar_feriados()
        self._cargar_fases_lunares()
        self._cargar_calendario_pesca()
    
    def _cargar_feriados(self):
        """Carga feriados en lista enlazada"""
        feriados_fijos = {
            1: [(1, "Año Nuevo")],
            5: [(1, "Día del Trabajo")],
            7: [(20, "Día de la Independencia")],
            8: [(7, "Batalla de Boyacá")],
            12: [(8, "Inmaculada Concepción"), (25, "Navidad")]
        }
        
        if self.mes in feriados_fijos:
            for dia, nombre in feriados_fijos[self.mes]:
                nuevo = NodoFecha(dia, nombre, "feriado")
                if not self.cabeza_feriados:
                    self.cabeza_feriados = nuevo
                else:
                    actual = self.cabeza_feriados
                    while actual.siguiente:
                        actual = actual.siguiente
                    actual.siguiente = nuevo
    
    def _cargar_fases_lunares(self):
        """Carga fases lunares en lista enlazada"""
        fases = [
            (7, "Luna Nueva"),
            (14, "Cuarto Creciente"),
            (21, "Luna Llena"),
            (28, "Cuarto Menguante")
        ]
        
        dias_mes = calendar.monthrange(self.anio, self.mes)[1]
        
        for dia, fase in fases:
            if dia <= dias_mes:
                nuevo = NodoFecha(dia, fase, "fase_lunar")
                if not self.cabeza_fases:
                    self.cabeza_fases = nuevo
                else:
                    actual = self.cabeza_fases
                    while actual.siguiente:
                        actual = actual.siguiente
                    actual.siguiente = nuevo
    
    def _cargar_calendario_pesca(self):
        """Carga calendario de pesca en lista enlazada"""
        dias_mes = calendar.monthrange(self.anio, self.mes)[1]
        
        for dia in range(1, dias_mes + 1):
            if dia in [7, 21]:
                nivel = "Excelente"
            elif dia in [14, 28]:
                nivel = "Bueno"
            else:
                nivel = "Regular"
            
            nuevo = NodoFecha(dia, nivel, "pesca")
            if not self.cabeza_pesca:
                self.cabeza_pesca = nuevo
            else:
                actual = self.cabeza_pesca
                while actual.siguiente:
                    actual = actual.siguiente
                actual.siguiente = nuevo
    
    def obtener_dia_actual(self) -> Dict:
        """Obtiene información del día actual"""
        dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 
                       'Viernes', 'Sábado', 'Domingo']
        dia_semana = dias_semana[self.fecha_actual.weekday()]
        
        return {
            'numero': self.fecha_actual.day,
            'dia_semana': dia_semana,
            'fecha_completa': self.fecha_actual.strftime("%d/%m/%Y")
        }
    
    def obtener_dias_feriados(self) -> List[str]:
        """Obtiene los días feriados recorriendo la lista enlazada"""
        feriados = []
        actual = self.cabeza_feriados
        
        while actual:
            feriados.append(f"Día {actual.dia}: {actual.info}")
            actual = actual.siguiente
        
        return feriados if feriados else ["No hay feriados este mes"]
    
    def obtener_fases_lunares(self) -> List[str]:
        """Obtiene fases lunares recorriendo la lista enlazada"""
        fases = []
        actual = self.cabeza_fases
        
        while actual:
            fases.append(f"Día {actual.dia}: {actual.info}")
            actual = actual.siguiente
        
        return fases
    
    def obtener_calendario_pesca(self) -> List[str]:
        """Obtiene calendario de pesca recorriendo la lista enlazada"""
        calendario = []
        actual = self.cabeza_pesca
        contador = 0
        
        while actual and contador < 10:
            calendario.append(f"Día {actual.dia}: {actual.info}")
            actual = actual.siguiente
            contador += 1
        
        return calendario
