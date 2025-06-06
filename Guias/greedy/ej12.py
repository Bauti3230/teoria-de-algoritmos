"""
Sabemos que los guardias trabajan una vez por mes, empiezan un
dia determinado y terminan otro (esto lo hacen de corrido).
Suponiendo que recibimos un arreglo de tuplas [(dia_ini,fia_fin),...,], 
que mas de un guardia puede trabajar el mismo dia. Queremos 
minimizar la cantidad de guardias en las instalaciones.

Recibimos un n siendo el dia final del mes y la lista de guardias

Idea : 
    Propongo ordenar los guardias por tiempo que permenencen en 
    el club y agregarlos solo si estan fuera del intervalo cubierto
"""

def actualizar_intervalo(intervalo_or,intervalo_nw):
    if intervalo_or[0] > intervalo_nw[0]:
        intervalo_or[0] = intervalo_nw[0]
    
    if intervalo_or[1] < intervalo_nw[1]:
        intervalo_or[1] = intervalo_nw[1]
    
    return

def minimizar_guardias(guardias,n):
    guardias.sort(key=lambda x:(x[0],-x[1]))

    solucion = []
    dia_actual = 1
    dia_fin = n
    i = 0    

    while(dia_actual <= n):
        mejor_fin = 0
        mejor_intervalo = None
        
        while i < len(guardias) and guardias[i][0] <= dia_actual:
            if guardias[i][1] >= mejor_fin:
                mejor_fin = guardias[i][1]
                mejor_intervalo = guardias[i]
            i += 1

        if mejor_intervalo is None:
            return None
        
        solucion.append(mejor_intervalo)
        dia_actual = mejor_intervalo[1] + 1

        if mejor_intervalo[1] >= n:
            return solucion
        
    return None