def costo_min(precio_camino):
    precio_camino.sort(reversed=True)

    costo = 0
    anios = 0

    for precio in precio_camino:
        costo += precio * (2**anios)
        anios += 1

    return costo