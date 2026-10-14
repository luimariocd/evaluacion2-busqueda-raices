# Evaluación 2: Búsqueda de Raíces
**Integrantes:**
- Luismario Huenuhueque (RUT: 21.895.671-8)
- Nicolás Muñoz (RUT: 21.964.601-1)

Este repositorio contiene la implementación y comparación de seis métodos numéricos para la búsqueda de raíces, aplicados sobre diferentes tipos de funciones matemáticas.

## Estructura del Proyecto

- `informe.md`: Contiene el análisis de convergencia y conclusiones.
- `requirements.txt`: Dependencias necesarias (`numpy`, `matplotlib`).
- `src/scripts/metodos.py`: Implementación matemática de los algoritmos (bisección, falsa posición, punto fijo, secante, Newton-Raphson, Newton mejorado).
- `src/scripts/main.py`: Script principal que evalúa las funciones, genera los datos y exporta las gráficas.
- `src/data/`: Archivos CSV generados con los puntos evaluados por función y el resumen de convergencia.
- `src/assets/`: Gráficos PNG que muestran cada función y la curva de error de los métodos.

## Entorno y Reproducción (Entorno Virtual)

Para reproducir este proyecto, se recomienda usar un entorno virtual (venv):

1. Clona el repositorio y navega a la carpeta principal:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd evaluacion2-busqueda-raices