vdef comite_min(horarios,N):
    horarios.sort(key=lambda x:x[1] - x[0],reverse=True)
    mayor_sup = 0
    solucion = []
    

    for horario_i in horarios:
        supervisados = 0
        for horario_j in horarios:

            if horario_i[1] >= horario_j[0] or horario_i[0] <= horario_j[1]:
                supervisados += 1
        
        if mayor_sup < supervisados+1:
            solucion.clear()
            mayor_sup = supervisados+1
            solucion.append(horario_i)
    
    return N-mayor_sup == 0, solucion


horarios = [(16, 20), (18, 22), (21, 23)]
comite = comite_min(horarios,3)
print("Comité mínimo:", comite)
# Resultado esperado: [(18, 22)]



