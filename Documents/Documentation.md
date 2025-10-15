# Proyecto Estructuras de Datos (MVC)

Este repositorio implementa una aplicación de consola en Python usando el patrón Modelo-Vista-Controlador (MVC). La aplicación permite gestionar archivos, calendarios, polinomios y matrices mediante menús interactivos.

## Estructura de carpetas

- *src/Model/*  
  Contiene las clases de lógica y almacenamiento de datos:
  - TDAArchivo, TDACalendario, TDAPolinomio, TDAMatriz  
  - Nodos auxiliares: NodoArchivo, NodoFecha, NodoTermino, NodoFila, NodoColumna

- *src/View/*  
  Incluye la clase Vista, responsable de mostrar menús y mensajes, y de leer la entrada del usuario.

- *src/Controller/*  
  Contiene la clase Controlador, que coordina la interacción entre la vista y los modelos.

## Principales funcionalidades

- *Gestión de archivos*: Abrir, leer, modificar y guardar datos en archivos simulados por listas enlazadas.
- *Calendario*: Consultar días feriados, fases lunares y días de pesca.
- *Polinomios*: Crear, sumar, restar, dividir y eliminar términos de polinomios.
- *Matrices*: Crear matrices, cargar valores aleatorios, sumar, restar y multiplicar.

## Ejecución

1. Clona el repositorio.
2. Ubícate en la carpeta raíz y ejecuta el archivo principal, por ejemplo:
   bash
   python src/main.py
   
3. Sigue las instrucciones del menú en consola.

## Notas

- El código utiliza estructuras enlazadas para almacenar datos.
- El patrón MVC separa la lógica de la interfaz y la gestión de datos.

---
