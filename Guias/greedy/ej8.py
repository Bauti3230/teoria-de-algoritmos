
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
        no_conocidos_solucion = len([s for s in solucion if s not in conocidos])

        if (conocidos_solucion >= 4 and no_conocidos_solucion >= 4) or aux(solucion,conocidos_dict,invitado):
            solucion.append(invitado) 
    
    return solucion