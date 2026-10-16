import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from metodos import biseccion, falsa_posicion, punto_fijo, secante, newton_raphson, newton_mejorado

# Rutas relativas asumiendo ejecución desde src/scripts/
PATH_DATA = "src/data"
PATH_ASSETS = "src/assets"

# Definición del ambiente controlado para las 6 funciones
funciones = {
    "Polinomica_Simple": {
        "f": lambda x: x**3 - x - 2, "df": lambda x: 3*x**2 - 1, "ddf": lambda x: 6*x, "g": lambda x: (x + 2)**(1/3),
        "a": 1, "b": 2, "x0": 1.5, "x1": 2.0, "x_rango": np.linspace(0, 3, 100)
    },
    "Polinomica_Doble": {
        "f": lambda x: (x - 2)**2, "df": lambda x: 2*x - 4, "ddf": lambda x: 2.0, "g": lambda x: (x**2 + 4)/4,
        "a": 1, "b": 3, "x0": 1.2, "x1": 2.5, "x_rango": np.linspace(0, 4, 100)
    },
    "Logaritmica": {
        "f": lambda x: np.log(x) + x - 4, "df": lambda x: 1/x + 1, "ddf": lambda x: -1/x**2, "g": lambda x: np.exp(4 - x),
        "a": 2, "b": 3, "x0": 2.5, "x1": 3.0, "x_rango": np.linspace(0.1, 4, 100)
    },
    "Exponencial": {
        "f": lambda x: np.exp(-x) - x, "df": lambda x: -np.exp(-x) - 1, "ddf": lambda x: np.exp(-x), "g": lambda x: np.exp(-x),
        "a": 0, "b": 1, "x0": 0.5, "x1": 1.0, "x_rango": np.linspace(-1, 2, 100)
    },
    "Trigonometrica": {
        "f": lambda x: np.cos(x) - x, "df": lambda x: -np.sin(x) - 1, "ddf": lambda x: -np.cos(x), "g": lambda x: np.cos(x),
        "a": 0, "b": 1, "x0": 0.5, "x1": 1.0, "x_rango": np.linspace(-1, 2, 100)
    },
    "Mixta": {
        "f": lambda x: np.sqrt(x) - np.cos(x), "df": lambda x: 1/(2*np.sqrt(x)) + np.sin(x), "ddf": lambda x: -1/(4*x**(1.5)) + np.cos(x), "g": lambda x: np.cos(x)**2,
        "a": 0.1, "b": 1, "x0": 0.5, "x1": 1.0, "x_rango": np.linspace(0.1, 2, 100)
    }
}

resumen_convergencia = []

for nombre, props in funciones.items():
    f, df, ddf, g = props["f"], props["df"], props["ddf"], props["g"]
    a, b, x0, x1 = props["a"], props["b"], props["x0"], props["x1"]
    
    # 1. Exportar CSV de (x, f(x)) por función
    ruta_csv_fx = os.path.join(PATH_DATA, f"{nombre}_datos.csv")
    with open(ruta_csv_fx, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["x", "f(x)"])
        for x_val in props["x_rango"]:
            writer.writerow([x_val, f(x_val)])
            
    # 2. Graficar función y marcar raíz (tangencia al eje en doble)
    plt.figure(figsize=(8, 5))
    plt.plot(props["x_rango"], f(props["x_rango"]), label=f"f(x) {nombre}")
    plt.axhline(0, color='black', linewidth=1)
    # Marcar raíz estimada (usamos Newton Mejorado como referencia segura para graficar)
    raiz_ref, _, _ = newton_mejorado(f, df, ddf, x0)
    if raiz_ref is not None:
        plt.scatter([raiz_ref], [f(raiz_ref)], color='red', zorder=5, label=f"Raíz en x ≈ {raiz_ref:.4f}")
    plt.title(f"Función: {nombre}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(PATH_ASSETS, f"{nombre}_funcion.png"))
    plt.close()

    # 3. Ejecutar métodos y registrar convergencia
    resultados = {
        "Biseccion": biseccion(f, a, b),
        "Falsa Posicion": falsa_posicion(f, a, b),
        "Punto Fijo": punto_fijo(g, x0),
        "Secante": secante(f, x0, x1),
        "Newton-Raphson": newton_raphson(f, df, x0),
        "Newton Mejorado": newton_mejorado(f, df, ddf, x0)
    }
    
    # 4. Graficar |error| vs iteración
    plt.figure(figsize=(10, 6))
    for met, (raiz, iteraciones, errores) in resultados.items():
        if raiz is not None and len(errores) > 0:
            plt.plot(range(1, len(errores) + 1), errores, marker='o', label=met)
            # Guardar datos para CSV resumen
            resumen_convergencia.append([nombre, met, iteraciones, raiz, errores[-1]])
        else:
            resumen_convergencia.append([nombre, met, "Fallo/No Aplica", "N/A", "N/A"])
            
    plt.yscale('log')
    plt.title(f"Convergencia de Métodos - {nombre}")
    plt.xlabel("Iteración")
    plt.ylabel("Error Absoluto (|xn - xn-1|)")
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig(os.path.join(PATH_ASSETS, f"{nombre}_convergencia.png"))
    plt.close()

# 5. Exportar CSV resumen de convergencia
ruta_csv_resumen = os.path.join(PATH_DATA, "resumen_convergencia.csv")
with open(ruta_csv_resumen, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Funcion", "Metodo", "Iteraciones", "Raiz Encontrada", "Error Final"])
    writer.writerows(resumen_convergencia)

print("Ejecución completada Archivos generados en 'data/' y 'assets/'.")