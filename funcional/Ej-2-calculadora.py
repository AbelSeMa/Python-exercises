"""
Escribir una función que simule una calculadora científica 
que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. 
La función preguntará al usuario el valor y la función a aplicar, 
y mostrará por pantalla una tabla con los enteros de 1 al valor introducido 
y el resultado de aplicar la función a esos enteros.

"""
import math

def calculadora():
    print("""
            Estás son las funciones que puedes utilizar:
            Seno => sen
            Coseno => cos
            Tangente => tan
            Exponencial => exp
            Logaritmo => log
          """)
    valor = int(input("Introduce el valor: "))
    funcion = input("¿Qué función deseas aplicar al valor?: ")
    opciones = ["sen", "cos", "tan", "exp", "log"]
    while funcion in opciones:
        if funcion == "sen":
            return math.sin(valor)
        elif funcion == "cos":
            return math.cos(valor)
        elif funcion == "tan":
            return math.tan(valor)
        elif funcion == "exp":
            return math.exp(valor)
        elif funcion == "log":
            return math.log(valor)
        else:
            print("No se ha reconocido la función introducida. Vuelve a intenarlo: ")


print(calculadora())