"""
queremos maximizar la cantidad de invitados, pero para que un invitado 
venga debe al menos connocer a 4 invitados. podemos decir que el arreglo de invitados
tiene la siguente forma : 
    [(nombre_invitado, [nombre_1,nombre_2,...,nombre_n]), ..., (...)]
es decir se tiene al invitado y las lista de gente que conoce.
"""

"""
all(len([c for c in conocidos_dict[inv] if c in solucion or c == invitado]) >= 4 for inv in solucion)):
"""

def aux(solucion,conocidos_dict,invitado):
    if len(solucion) < 4: return False

    for inv in solucion:
        if len([c for c in conocidos_dict[inv] if c in solucion or c == invitado]) < 4:
            return False
    
    return True


def maximizar_invitados(invitados):
    invitados.sort(key=lambda x:len(x[1]), reverse=True)
    solucion = []

    conocidos_dict = {inv[0]: inv[1] for inv in invitados }


    for invitado, conocidos in invitados:

        conocidos_solucion = len([c for c in conocidos if c in solucion])

        if conocidos_solucion >= 4 or aux(solucion,conocidos_dict,invitado):
            solucion.append(invitado) 
    
    return solucion