def triangle():
    a = float(input())
    b = float(input())
    c = float(input())
    if a + b > c and a + c > b and b + c > a:
        print("Los lados forman un triangulo valido")
    else:
        print("Los lados no forman un triangulo valido")
