"""
queremos maximizar la cantidad de invitados, pero para que un invitado 
venga debe al menos connocer a 4 invitados. podemos decir que el arreglo de invitados
tiene la siguente forma : 
    [(nombre_invitado, [nombre_1,nombre_2,...,nombre_n]), ..., (...)]
es decir se tiene al invitado y las lista de gente que conoce.
"""
def maximizar_invitados(invitados):
    invitados.sort(key=lambda x:len(x[1]), reverse=True)
    solucion = []

    for invitado in invitados:
        if len(invitado[1]) < 4:
            continue
        solucion.append(invitado[0])
    
    return invitado