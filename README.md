# Nodo

Bienvenido a **Nodo**, un sistema de demostración y práctica de Tipos de Datos Abstractos (TDAs) implementados con nodos y listas enlazadas en Python. El proyecto está orientado a estudiantes y desarrolladores interesados en la estructura interna de los TDAs, mostrando cómo se pueden construir y manipular archivos, calendarios, polinomios y matrices utilizando nodos.

## Tabla de Contenidos

- [Características](#características)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Características

- **TDA Archivo:** Manejo de archivos usando listas enlazadas y `shelve` para almacenamiento persistente.
- **TDA Calendario:** Gestión de fechas, días feriados y fases lunares como listas enlazadas.
- **TDA Polinomio:** Operaciones algebraicas con polinomios representados como listas enlazadas de términos.
- **TDA Matriz:** Creación y manipulación de matrices (suma, resta, multiplicación) implementadas con listas enlazadas de filas y columnas de nodos.
- **Arquitectura MVC:** Separación clara de la lógica de negocio (Model), la interfaz de usuario (View) y el flujo de control (Controller).

## Estructura del Proyecto

```
Nodo/
├── src/
│   ├── Controller/
│   │   └── controlador.py
│   ├── Model/
│   │   ├── archivo.py
│   │   ├── calendario.py
│   │   ├── matriz.py
│   │   ├── nodos.py
│   │   └── polinomio.py
│   ├── View/
│   │   └── vista.py
│   └── main.py
```

- **main.py:** Punto de entrada del sistema.
- **Controller/**: Lógica de control y menús para cada TDA.
- **Model/**: Implementaciones de los TDAs con nodos y sus clases asociadas.
- **View/**: Interfaz de consola para interactuar con el usuario.

## Diagrama de clases

<img width="1232" height="892" alt="image" src="https://github.com/user-attachments/assets/9c52a034-ad77-4403-9c6e-cf79a58bad87" />



## Instalación

1. **Requisitos previos:**
   - Python 3.8 o superior.

2. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Valenbu325/Nodo.git
   cd Nodo
   ```

3. **Instalar dependencias (si aplica):**
   Actualmente, el proyecto solo depende de la librería estándar de Python (`shelve`, `calendar`, `datetime`, etc.).

## Uso

Ejecuta el sistema desde la raíz del proyecto:

```bash
python src/main.py
```

Verás un menú principal con las siguientes opciones:

1. **TDA Archivo (Shelve + Nodos):** Abrir, guardar, leer, modificar y listar datos almacenados en archivos usando una lista enlazada.
2. **TDA Calendario (Nodos):** Consultar el día actual, días feriados, fases lunares y calendario de pesca.
3. **TDA Polinomio (Nodos):** Crear polinomios, sumar, restar, multiplicar, dividir, eliminar y buscar términos.
4. **TDA Matriz (Nodos):** Crear matrices A y B, cargarlas aleatoriamente, realizar operaciones entre ellas y mostrar resultados.
0. **Salir:** Termina la aplicación.

### Ejemplo de flujo

```text
============================================================
  BIENVENIDO AL SISTEMA DE TDAs CON ESTRUCTURAS DINÁMICAS
  Todos los TDAs implementados con NODOS y LISTAS ENLAZADAS
============================================================
```

Sigue las instrucciones en pantalla para navegar entre los TDAs y realizar operaciones.

## Contribución

¡Las contribuciones son bienvenidas! Si deseas colaborar:

1. Haz un fork del repositorio.
2. Crea una rama para tu funcionalidad o corrección (`git checkout -b mi-feature`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Haz push a tu rama (`git push origin mi-feature`).
5. Abre un Pull Request en este repositorio.

## Licencia

Este proyecto actualmente **no declara una licencia**. Por favor, contacta a [Valenbu325](https://github.com/Valenbu325) si tienes dudas sobre su uso.

---

## Autores

Valentina Burgos
Andres Moreno

Desarrollado como herramienta educativa para el aprendizaje de estructuras dinámicas y TDAs en Python.
