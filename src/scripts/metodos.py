import numpy as np

def biseccion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        return None, 0, []  # Falla si no hay cambio de signo
    
    errores = []
    x_prev = a
    for i in range(max_iter):
        c = (a + b) / 2
        error = abs(c - x_prev)
        errores.append(error)
        
        if error < tol or abs(f(c)) < tol:
            return c, i + 1, errores
            
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
        x_prev = c
    return c, max_iter, errores

def falsa_posicion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        return None, 0, []
    
    errores = []
    x_prev = a
    for i in range(max_iter):
        c = b - (f(b) * (a - b)) / (f(a) - f(b))
        error = abs(c - x_prev)
        errores.append(error)
        
        if error < tol or abs(f(c)) < tol:
            return c, i + 1, errores
            
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        x_prev = c
    return c, max_iter, errores

def punto_fijo(g, x0, tol=1e-6, max_iter=100):
    errores = []
    x_prev = x0
    for i in range(max_iter):
        try:
            x_new = g(x_prev)
            error = abs(x_new - x_prev)
            errores.append(error)
            
            if error < tol:
                return x_new, i + 1, errores
            x_prev = x_new
        except OverflowError: # Por si el método diverge dramáticamente
            return None, i + 1, errores 
    return x_prev, max_iter, errores

def secante(f, x0, x1, tol=1e-6, max_iter=100):
    errores = []
    for i in range(max_iter):
        if f(x1) - f(x0) == 0:
            return None, i + 1, errores # Evitar división por cero
            
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        error = abs(x2 - x1)
        errores.append(error)
        
        if error < tol or abs(f(x2)) < tol:
            return x2, i + 1, errores
            
        x0, x1 = x1, x2
    return x2, max_iter, errores

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    errores = []
    x_prev = x0
    for i in range(max_iter):
        if df(x_prev) == 0:
            return None, i + 1, errores
            
        x_new = x_prev - f(x_prev) / df(x_prev)
        error = abs(x_new - x_prev)
        errores.append(error)
        
        if error < tol or abs(f(x_new)) < tol:
            return x_new, i + 1, errores
            
        x_prev = x_new
    return x_prev, max_iter, errores

def newton_mejorado(f, df, ddf, x0, tol=1e-6, max_iter=100):
    # Newton-Raphson Modificado para raíces múltiples
    errores = []
    x_prev = x0
    for i in range(max_iter):
        denominador = (df(x_prev)**2 - f(x_prev) * ddf(x_prev))
        if denominador == 0:
            return None, i + 1, errores
            
        x_new = x_prev - (f(x_prev) * df(x_prev)) / denominador
        error = abs(x_new - x_prev)
        errores.append(error)
        
        if error < tol or abs(f(x_new)) < tol:
            return x_new, i + 1, errores
            
        x_prev = x_new
    return x_prev, max_iter, errores