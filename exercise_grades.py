def grades():
    """
    Ejercicio 5 - Clasificar Notas

    Leer una nota (0-10) mediante input(). Clasificar la nota e imprimir:
    - "Excelente" si está entre 9 y 10
    - "Bueno" si está entre 7 y 8
    - "Regular" si está entre 5 y 6
    - "Insuficiente" si está entre 0 y 4

    Ejemplo:
        Para la entrada "9", la salida esperada es:
        Excelente

        Para la entrada "6", la salida esperada es:
        Regular

        Para la entrada "3", la salida esperada es:
        Insuficiente
    """
    nota = int(input("Ingrese nota: "))
    if nota <= 10 and nota >= 9:
        print("Excelente")
    elif nota <= 8 and nota >=7:
        print("Bueno")
    elif nota <=6 and nota >=5:
        print("Regular")
    elif nota <=4 and nota >=0:
        print("Insuficiente")

if __name__ == "__main__":
    grades()