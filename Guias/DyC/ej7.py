def merge(arr_izq,arr_der):
    resultado = []

    i = j = 0
    h1 = h2 = 0

    while i < len(arr_izq) and j < len(arr_der):
        if arr_izq[i][0] < arr_der[j][0] :
            x, h1 = arr_izq[i]
            i += 1
        elif arr_der[j][0] < arr_izq[i][0] :
            x, h2 = arr_der[j]
            j += 1
        else :
            x = arr_izq[i][0]
            h1 = arr_izq[i][1]
            h2 = arr_der[j][2]

            i += 1
            j += 1

        max_altura = max(h1,h2)

        if not resultado or resultado[-1][1] != max_altura:
            resultado.append((x, max_altura))
    
    if i < len(arr_izq):
        resultado.extend(arr_izq[i:])
    
    if j < len(arr_der):
        resultado.extend(arr_der[j:])

    return resultado

def contorno_ciudad(stats,ini,fin):
    if ini >= fin:
        edifico = stats[ini]
        ini_intervalo = (edifico[0],edifico[1])
        fin_intervalo = (edifico[2],0)

        return [ini_intervalo,fin_intervalo]
    
    mid = (ini + fin) // 2

    arr_izq = contorno_ciudad(stats,ini,mid)
    arr_der = contorno_ciudad(stats,mid+1,fin)

    return merge(arr_izq,arr_der)

edificios = [(1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16), (14, 3, 25), (19, 18, 22)]
print(contorno_ciudad(edificios,0,len(edificios)-1))