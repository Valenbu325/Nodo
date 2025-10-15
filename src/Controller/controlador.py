from View.Vista import Vista 
from Model.archivo import TDAArchivo 
from Model.calendario import TDACalendario  
from Model.polinomio import TDAPolinomio  
from Model.matriz import TDAMatriz



class Controlador:
    """Controlador principal del sistema MVC"""
    
    def __init__(self):
        self.vista = Vista()
        self.tda_archivo = TDAArchivo()
        self.tda_calendario = TDACalendario()
        self.polinomio1 = TDAPolinomio()
        self.polinomio2 = TDAPolinomio()
        self.matriz_a = None
        self.matriz_b = None
    
    def ejecutar(self):
        """Ejecuta el programa principal"""
        while True:
            self.vista.mostrar_menu_principal()
            opcion = self.vista.leer_entrada("Seleccione una opción: ")
            
            if opcion == "1":
                self.menu_archivo()
            elif opcion == "2":
                self.menu_calendario()
            elif opcion == "3":
                self.menu_polinomio()
            elif opcion == "4":
                self.menu_matriz()
            elif opcion == "0":
                self.vista.mostrar_mensaje("¡Hasta pronto!")
                break
            else:
                self.vista.mostrar_mensaje("Opción inválida")
    
    def menu_archivo(self):
        while True:
            self.vista.mostrar_menu_archivo()
            opcion = self.vista.leer_entrada("Seleccione una opción: ")
            
            if opcion == "1":
                ruta = self.vista.leer_entrada("Ingrese ruta del archivo: ")
                exito, msg = self.tda_archivo.abrir(ruta)
                self.vista.mostrar_mensaje(msg)
            elif opcion == "2":
                clave = self.vista.leer_entrada("Ingrese clave: ")
                dato = self.vista.leer_entrada("Ingrese dato: ")
                exito, msg = self.tda_archivo.guardar(dato, clave)
                self.vista.mostrar_mensaje(msg)
            elif opcion == "3":
                clave = self.vista.leer_entrada("Ingrese clave: ")
                dato, msg = self.tda_archivo.leer(clave)
                self.vista.mostrar_mensaje(f"{msg}\nDato: {dato}")
            elif opcion == "4":
                clave = self.vista.leer_entrada("Ingrese clave: ")
                dato = self.vista.leer_entrada("Ingrese nuevo dato: ")
                exito, msg = self.tda_archivo.modificar(clave, dato)
                self.vista.mostrar_mensaje(msg)
            elif opcion == "5":
                datos = self.tda_archivo.listar_datos()
                if datos:
                    self.vista.mostrar_mensaje("Datos almacenados:\n" + "\n".join(datos))
                else:
                    self.vista.mostrar_mensaje("No hay datos almacenados")
            elif opcion == "6":
                exito, msg = self.tda_archivo.cerrar()
                self.vista.mostrar_mensaje(msg)
            elif opcion == "0":
                break
    
    def menu_calendario(self):
        while True:
            self.vista.mostrar_menu_calendario()
            opcion = self.vista.leer_entrada("Seleccione una opción: ")
            
            if opcion == "1":
                info = self.tda_calendario.obtener_dia_actual()
                self.vista.mostrar_mensaje(
                    f"Día {info['numero']} - {info['dia_semana']}\n"
                    f"Fecha: {info['fecha_completa']}"
                )
            elif opcion == "2":
                feriados = self.tda_calendario.obtener_dias_feriados()
                self.vista.mostrar_mensaje("Días feriados:\n" + "\n".join(feriados))
            elif opcion == "3":
                fases = self.tda_calendario.obtener_fases_lunares()
                self.vista.mostrar_mensaje("Fases lunares:\n" + "\n".join(fases))
            elif opcion == "4":
                calendario = self.tda_calendario.obtener_calendario_pesca()
                self.vista.mostrar_mensaje("Calendario de pesca (primeros 10 días):\n" + "\n".join(calendario))
            elif opcion == "0":
                break
    
    def menu_polinomio(self):
        while True:
            self.vista.mostrar_menu_polinomio()
            opcion = self.vista.leer_entrada("Seleccione una opción: ")
            
            if opcion == "1":
                self.crear_polinomio(1)
            elif opcion == "2":
                self.crear_polinomio(2)
            elif opcion == "3":
                resultado = self.polinomio1.sumar(self.polinomio2)
                self.vista.mostrar_mensaje(f"P1 + P2 = {resultado}")
            elif opcion == "4":
                resultado = self.polinomio1.restar(self.polinomio2)
                self.vista.mostrar_mensaje(f"P1 - P2 = {resultado}")
            elif opcion == "5":
                resultado, msg = self.polinomio1.dividir(self.polinomio2)
                if resultado:
                    self.vista.mostrar_mensaje(f"{msg}\nP1 ÷ P2 = {resultado}")
                else:
                    self.vista.mostrar_mensaje(msg)
            elif opcion == "6":
                exp = int(self.vista.leer_entrada("Exponente a eliminar del P1: "))
                exito = self.polinomio1.eliminar_termino(exp)
                self.vista.mostrar_mensaje(
                    f"Término con exponente {exp} eliminado" if exito else "Término no encontrado"
                )
            elif opcion == "7":
                exp = int(self.vista.leer_entrada("Exponente a buscar en P1: "))
                existe = self.polinomio1.existe_termino(exp)
                self.vista.mostrar_mensaje(
                    f"El término con exponente {exp} {'EXISTE' if existe else 'NO EXISTE'} en P1"
                )
            elif opcion == "8":
                self.vista.mostrar_mensaje(
                    f"Polinomio 1: {self.polinomio1}\n"
                    f"Polinomio 2: {self.polinomio2}"
                )
            elif opcion == "0":
                break
    
    def crear_polinomio(self, num):
        """Crea un polinomio solicitando términos al usuario"""
        poli = self.polinomio1 if num == 1 else self.polinomio2
        poli.cabeza = None
        
        n = int(self.vista.leer_entrada(f"Cantidad de términos para P{num}: "))
        
        for i in range(n):
            print(f"\nTérmino {i+1}:")
            coef = float(self.vista.leer_entrada("  Coeficiente: "))
            exp = int(self.vista.leer_entrada("  Exponente: "))
            poli.insertar_termino(coef, exp)
        
        self.vista.mostrar_mensaje(f"Polinomio {num} creado: {poli}")
    
    def menu_matriz(self):
        while True:
            self.vista.mostrar_menu_matriz()
            opcion = self.vista.leer_entrada("Seleccione una opción: ")
            
            if opcion == "1":
                n = int(self.vista.leer_entrada("Tamaño de matriz A (n×n): "))
                self.matriz_a = TDAMatriz(n)
                self.vista.mostrar_mensaje(f"Matriz A de {n}×{n} creada con nodos")
            elif opcion == "2":
                n = int(self.vista.leer_entrada("Tamaño de matriz B (n×n): "))
                self.matriz_b = TDAMatriz(n)
                self.vista.mostrar_mensaje(f"Matriz B de {n}×{n} creada con nodos")
            elif opcion == "3":
                if self.matriz_a:
                    self.matriz_a.cargar_aleatoria()
                    self.vista.mostrar_mensaje("Matriz A cargada aleatoriamente")
                if self.matriz_b:
                    self.matriz_b.cargar_aleatoria()
                    self.vista.mostrar_mensaje("Matriz B cargada aleatoriamente")
                if not self.matriz_a and not self.matriz_b:
                    self.vista.mostrar_mensaje("No hay matrices creadas")
            elif opcion == "4":
                if self.matriz_a and self.matriz_b:
                    resultado, msg = self.matriz_a.sumar(self.matriz_b)
                    if resultado:
                        self.vista.mostrar_mensaje(f"{msg}\n\nA + B =\n{resultado}")
                    else:
                        self.vista.mostrar_mensaje(msg)
                else:
                    self.vista.mostrar_mensaje("Debe crear ambas matrices primero")
            elif opcion == "5":
                if self.matriz_a and self.matriz_b:
                    resultado, msg = self.matriz_a.restar(self.matriz_b)
                    if resultado:
                        self.vista.mostrar_mensaje(f"{msg}\n\nA - B =\n{resultado}")
                    else:
                        self.vista.mostrar_mensaje(msg)
                else:
                    self.vista.mostrar_mensaje("Debe crear ambas matrices primero")
            elif opcion == "6":
                if self.matriz_a and self.matriz_b:
                    resultado, msg = self.matriz_a.multiplicar(self.matriz_b)
                    if resultado:
                        self.vista.mostrar_mensaje(f"{msg}\n\nA × B =\n{resultado}")
                    else:
                        self.vista.mostrar_mensaje(msg)
                else:
                    self.vista.mostrar_mensaje("Debe crear ambas matrices primero")
            elif opcion == "7":
                msg = ""
                if self.matriz_a:
                    msg += f"Matriz A:\n{self.matriz_a}\n"
                if self.matriz_b:
                    msg += f"Matriz B:\n{self.matriz_b}"
                if msg:
                    self.vista.mostrar_mensaje(msg)
                else:
                    self.vista.mostrar_mensaje("No hay matrices creadas")
            elif opcion == "0":
                break