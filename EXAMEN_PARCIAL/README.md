# Examen Parcial - Gestión de Biblioteca

Este directorio contiene el avance casi completo del examen parcial del curso **Programación Orientada a Objetos**.
El proyecto implementa una pequeña aplicación de biblioteca escrita en **Python** empleando **PyQt5** para la interfaz gráfica.

## Estructura del proyecto

- **main.py**: punto de entrada de la aplicación.
- **CONTROLADOR/**: lógica de control que orquesta las acciones entre la interfaz y el modelo.
- **MODELO/**: definición de clases que representan libros, miembros y la biblioteca.
- **VISTA/** y **UI/**: archivos `*.py` y `*.ui` que conforman la interfaz gráfica.

## Funcionalidades actuales

- Registro de libros físicos y digitales.
- Registro de miembros.
- Préstamo y devolución de libros con actualización de estados.
- Visualización de los libros en una tabla dentro de la interfaz.

## Próximos pasos

- Incorporar una tabla paralela para mejorar la visualización de datos.
- Implementar persistencia mediante una base de datos de registros.
- Optimizar la interfaz gráfica para ofrecer una mejor experiencia de usuario (UI/UX).

## Ejecución

Requisitos principales:

- Python 3.x
- PyQt5

Para ejecutar la aplicación, situarse en este directorio y correr:

```bash
python3 main.py
```

Este repositorio seguirá actualizándose conforme se completen las funcionalidades faltantes.
