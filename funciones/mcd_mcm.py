# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
import timeit
def mcm(n, m):
    div = max(n, m)

    while n != 0:
        if (div % n == 0 and div % m == 0):
            return div
        div += max(n, m)

# Medir el tiempo de ejecución
tiempo = timeit.timeit(lambda: mcm(33, 85), number=10000)
print("Tiempo de ejecución:", tiempo)
