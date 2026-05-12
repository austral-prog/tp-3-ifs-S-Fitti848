def grades():
    nota = int(input())
    if nota >= 9:
        print("Excelente")
    elif nota >= 7:
        print("Bueno")
    elif nota >= 5:
        print("Regular")
    else:
        print("Insuficiente")
