"""
formato : 
    actividades = [(ini,fin,val),...,]
"""
def schedulig_pesado_bt(actividades,asignacion,asignacion_act,sum_act,max_sum,i):
    if not max_sum[0][0]  or sum_act > max_sum[0][0]:
        max_sum[0][0] = sum_act
        asignacion[0].clear()
        asignacion[0].extend(asignacion_act.copy())

    if i >= len(actividades):
        return
        
    
    for actividad in actividades:
        if actividad in asignacion_act:
            continue

        if no_conflict(actividad,asignacion_act):
            asignacion_act.append(actividad)
            sum_act += actividad[2]
            schedulig_pesado_bt(actividades,asignacion,asignacion_act,sum_act,max_sum,i+1)
            asignacion_act.pop()
            sum_act -= actividad[2]
    
    return

def no_conflict(actividad,asignacion):
    for asignado in asignacion:
        if asignado[1] > actividad[0]:
            return False
    return True
    

def wrapper_scheduling(actividades):
    actividades.sort(key=lambda x:x[1])

    i = 0
    res = None

    for actividad in actividades :
        schedulig_pesado_bt(actividades,[[]],[actividad],0 + actividad[2],[res],i+1)

act = [(1,4,5),(3,5,6),(0,6,8)]

wrapper_scheduling(act)
