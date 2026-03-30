"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividadjhghgh
"""

def contar_ciclo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando iteración.
    """
    lista = []
    for i in range(1,n+1):
        lista.append(i)
    return lista

def contar_recursivo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando recursividad.
    """
    lista = []
    if n == 1:
        lista.append(1)
        return lista
    else:
        lista.append(contar_recursivo(n-1))
        return lista

x = int(input("ingrese un numero: "))
print(contar_ciclo(x))
print(contar_recursivo(x))