def discount():
    precio = float(input())
    cantidad = int(input())
    subtotal = precio * cantidad
    if cantidad >= 10:
        descuento_pct = 20
    elif cantidad >= 5:
        descuento_pct = 10
    else:
        descuento_pct = 0
    monto_descuento = subtotal * descuento_pct / 100
    total = subtotal - monto_descuento
    print(f"Subtotal: {subtotal}")
    print(f"Descuento aplicado: {descuento_pct}%")
    print(f"Monto de descuento: {monto_descuento}")
    print(f"Total final: {total}")
