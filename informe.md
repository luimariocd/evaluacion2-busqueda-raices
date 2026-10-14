# Informe de Análisis de Convergencia

## 1. Preguntas de Convergencia

**¿Qué método convergió en menos iteraciones en cada función? ¿Por qué?**
En las raíces simples (Polinómica Simple, Logarítmica, Exponencial, Trigonométrica, Mixta), el método de Newton-Raphson (y el Mejorado) convergió en la menor cantidad de iteraciones. Esto ocurre porque utiliza la derivada de la función para trazar una recta tangente que apunta directamente hacia la raíz, acelerando drásticamente la búsqueda en comparación con los métodos que solo acortan intervalos.

**¿Qué orden de convergencia tiene cada método y cómo se refleja en el gráfico |error| vs iteración?**
- **Lineal:** Bisección, Falsa Posición y Punto Fijo. En los gráficos de escala logarítmica, su error desciende en una línea recta diagonal constante.
- **Superlineal:** Secante (orden ≈ 1.618). Su pendiente de caída es más pronunciada que la lineal.
- **Cuadrático:** Newton-Raphson y Newton Mejorado. En los gráficos, la curva de error de estos métodos cae verticalmente casi de golpe en las últimas iteraciones.

**¿Qué métodos requieren un intervalo con cambio de signo y cuáles no?**
Los métodos cerrados (Bisección y Falsa Posición) requieren obligatoriamente un intervalo $[a, b]$ donde $f(a) \cdot f(b) < 0$ (cambio de signo). Los métodos abiertos (Punto Fijo, Secante, Newton-Raphson y Newton Mejorado) no lo requieren; solo necesitan una o dos estimaciones iniciales ($x_0, x_1$).

**En la función que toca el eje x (raíz doble): ¿qué métodos fallan o no aplican y cuál se comporta mejor? ¿Por qué?**
Para la función polinómica doble $f(x) = (x-2)^2$:
- **Fallan/No aplican:** Bisección y Falsa Posición, ya que la función nunca cruza el eje Y hacia los negativos, imposibilitando el cambio de signo. Newton-Raphson tradicional se vuelve lento (cae a convergencia lineal) o falla por división por cero cerca de la raíz.
- **Se comporta mejor:** El método de Newton Mejorado. Al incorporar la segunda derivada en su fórmula, logra mantener el orden de convergencia cuadrático incluso en raíces múltiples.

**¿Cómo influyen el intervalo inicial y la estimación inicial en la cantidad de iteraciones y en si el método converge?**
Un intervalo más amplio o una estimación inicial muy lejana a la raíz aumenta directamente el número de iteraciones. En métodos abiertos como Newton o Punto Fijo, una mala estimación inicial (por ejemplo, cerca de un punto de inflexión o donde la derivada es cero) puede provocar que el método diverja hacia el infinito y nunca encuentre la raíz.

**¿Qué método recomiendan según el tipo de función, considerando el compromiso entre velocidad y robustez?**
- Si se busca **robustez total** y se garantiza un cambio de signo, la Bisección es la opción más segura, aunque lenta.
- Si se busca **velocidad** y es fácil calcular las derivadas analíticas, Newton-Raphson es superior.
- Como **compromiso ideal**, el método de la Secante ofrece una velocidad casi tan buena como Newton, pero sin la complejidad matemática de calcular y programar derivadas.

---

## 2. Conclusión

**¿Qué método elegirían para cada tipo de función y por qué (velocidad vs robustez)?**
Elegiría el método de la Secante para funciones exponenciales, logarítmicas y trigonométricas, ya que ofrece un excelente equilibrio: es rápido (convergencia superlineal) y evita el costo de calcular derivadas complejas en código. Para las funciones polinómicas, Newton-Raphson es preferible dada la extrema facilidad para derivar polinomios. Si la gráfica nos indica un comportamiento volátil, recurriríamos a Bisección por su robustez inquebrantable.

**¿Qué ocurrió en la raíz doble y qué dice eso sobre «tener raíz» frente a «cambiar de signo»?**
La raíz doble demostró que "tener una raíz" (que la función valga cero) no es sinónimo de "cambiar de signo" (cruzar el eje). Esto invalida por completo el teorema de Bolzano para la búsqueda de esas raíces específicas. Nos enseña que confiar exclusivamente en métodos de intervalos cerrados es un riesgo, y resalta la necesidad de métodos abiertos que analicen el comportamiento geométrico (tangentes) de la curva.

**¿Cómo cambió el número de iteraciones al mover el intervalo o la estimación inicial?**
Al probar con estimaciones iniciales más alejadas, métodos como Newton-Raphson incrementaron sus iteraciones para compensar la distancia inicial, pero su caída en picada en el gráfico de errores se mantuvo igual de abrupta al acercarse al cero. En contraparte, los métodos de intervalos requirieron más divisiones sucesivas a la mitad, sumando iteraciones de forma lineal y constante.