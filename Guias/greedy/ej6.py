def no_asignado(pack,solucion):
    for asignacion in solucion:
        pack_asignado = asignacion[1]
        if pack == pack_asignado : return False
    return True

def suscripciones(suscripciones_y_regalos, packs):
    solucion = []

    for suscipcion in suscripciones_y_regalos:
        for pack in packs:

            if pack in suscipcion[1] and no_asignado(pack,solucion):
                solucion.append((suscipcion[0],pack))
                break
    return solucion

if __name__ == "__main__":
    suscripciones_y_regalos = [ ("St", ["Pa"]), ("So", ["Pa", "Pb"]), ("Sp", ["Pa","Pg"]), ("Sb", ["Pa", "Pb", "Pg", "Pe"])]
    packs = ["Pa", "Pb", "Pg", "Pe"]

    resultado = suscripciones(suscripciones_y_regalos,packs=packs)

    print(resultado)        