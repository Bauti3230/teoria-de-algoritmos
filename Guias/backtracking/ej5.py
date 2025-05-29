def no_conflicto(asignaciones,trabajo,constratista):
    for asignacion in asignaciones: #asignaciones = [(nombre, id_trabajo)]
        if asignacion[0] == constratista[0] or asignacion[1] == trabajo:
            return False
    return True
 
def contratistas_bt(contratistas,trabajos,asignaciones_act,asignacion,gast_act,gasto_min,n,i):
    if len(asignaciones_act) == n:
        if gast_act < gasto_min[0][0] or gasto_min[0][0] == 0:
            gasto_min[0] = gast_act
            asignacion[0].clear()
            asignacion[0].extend(asignaciones_act.copy())
        return 

    if i >= n:
        return
    
    for contratista_act in contratistas:
        for trabajo in trabajos: # trabajos = [id_0,...,id_n] 0 <= id < n
            if no_conflicto(asignaciones_act,trabajo,contratista_act):
                asignaciones_act.append((contratista_act[0],trabajo))
                gast_act += contratista_act[1][trabajo]
                i += 1
                contratistas_bt(contratistas,trabajos,asignaciones_act,asignacion,gast_act,gasto_min,n,i)
                asignaciones_act.pop()
                gast_act -= contratista_act[1][trabajo]
                i -= 1
    
    return

trabajos = [0,1]
contrastistas = [('A',[5,6]),('B',[8,4])]
gasto_min = [0]

contratistas_bt(contrastistas,trabajos,[],[[None]],0,[[0]],2,0)


