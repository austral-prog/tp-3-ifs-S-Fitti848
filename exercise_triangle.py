def triangle():
    """
    Ejercicio 8 - Validar Triángulo

    Leer tres números que representan los lados de un triángulo mediante input().
    Verificar si pueden formar un triángulo válido e imprimir el resultado.
    Un triángulo es válido si la suma de dos lados cualesquiera es estrictamente mayor
    que el tercer lado (desigualdad triangular). Si la suma es igual, forman una línea
    recta, no un triángulo.

    Ejemplo:
        Para las entradas "3", "4" y "5", la salida esperada es:
        Los lados forman un triangulo valido

        Para las entradas "1", "2" y "5", la salida esperada es:
        Los lados no forman un triangulo valido
    """

    num1= float(input())
    num2= float(input())
    num3= float(input())

    if num1 + num2>num3 and num3 + num2>num1 and num1 + num3>num2:
        print("Los lados forman un triangulo valido")
    else:
        print("Los lados no forman un triangulo valido")

if __name__ == "__main__":
    triangle()