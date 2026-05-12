def password():
    pw = input()
    tiene_numero = False
    for d in "0123456789":
        if d in pw:
            tiene_numero = True
            break
    if len(pw) < 8 and tiene_numero:
        print("Contraseña muy corta")
    elif len(pw) >= 8 and not tiene_numero:
        print("Debe contener un numero")
    elif len(pw) < 8 and not tiene_numero:
        print("Contraseña muy corta")
        print("Debe contener un numero")
    else:
        print("Contraseña valida")
