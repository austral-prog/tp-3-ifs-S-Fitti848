def calculator():
    a = float(input())
    b = float(input())
    op = input()
    if op == "+":
        print(f"Resultado: {a + b}")
    elif op == "-":
        print(f"Resultado: {a - b}")
    elif op == "*":
        print(f"Resultado: {a * b}")
    elif op == "/":
        if b == 0:
            print("Error: division por cero")
        else:
            print(f"Resultado: {a / b}")
    else:
        print("Operacion invalida")
