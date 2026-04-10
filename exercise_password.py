def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    con=input()

    tiene_numero = "0" in con or "1" in con or "2" in con or "3" in con or "4" in con or "5" in con or "6" in con or "7" in con or "8" in con or "9" in con

    if len(con) >= 8 and tiene_numero:
        print("Contraseña valida")
    else:
        if len(con) < 8:
            print("Contraseña muy corta")
        if not tiene_numero:
            print("Debe contener un numero")

if __name__ == "__main__":
    password()
