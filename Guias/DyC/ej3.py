# [-1, 0, 1]    [-1, 1, 0]    
# [1, -1, 0]    [1, 0, -1]
# [0, 1, -1]    [0, -1, 1]

# [-1, 1, 0, 0]
# [0, -1, 1, 0]
# [1, 0, -1, 1]
# [1, 1, 0, -1]

# [-1, 0, 1, 1, 0]
# [1, -1, 0, 1, 1]
# [0, 1, -1, 0, 1]
# [0, 0, 1, -1, 0]
# [1, 0, 0, 1, -1]

def gana(a,b,resultados):
    idx_a = a-1
    idx_b = b-1
    resultados_a = resultados[idx_a]
    resultados_b = resultados[b-1]

    res_a_b = resultados_a[b-1]
    res_b_a = resultados_b[a-1]

    return res_a_b == 1 and res_b_a == 0



def ordenar_resultados(ini,fin,resultados,jugadores):
    if len(jugadores) <= 1:
        return jugadores
    
    mid = (ini + fin) // 2

    izq = ordenar_resultados(ini,mid-1,resultados,jugadores[:mid])
    der = ordenar_resultados(mid,fin,resultados,jugadores[mid:])

    return merge(izq,der,resultados)

def merge(izq,der,resultados):
    resultado = []
    
    i = j = 0

    while i < len(izq) and j < len(der):
        if gana(izq[i],der[j],resultados):
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    
    return resultado 

resultados = [[-1, 0, 1], [1, -1, 0], [0, 1, -1]]
jugadores = [1,2,3]

print(ordenar_resultados(0,len(jugadores),resultados,jugadores))