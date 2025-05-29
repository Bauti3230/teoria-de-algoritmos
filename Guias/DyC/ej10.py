def merge(arr_izq,arr_der,ranking_izq,ranking_der):
    resultado_ranking = ranking_izq + ranking_der
    resultado_idx = []

    i = j = 0

    while i < len(arr_izq) and j < len(arr_der):
        if ranking_izq[i][1] > ranking_der[j][1] and ranking_izq[i][0] < ranking_der[j][0]:
            arr_izq[i] += 1
            i += 1
        elif ranking_der[j][1] > ranking_izq[i][1] and ranking_der[j][0] < ranking_izq[i][0]:
            arr_der[j] += 1
            j += 1
        else:
            i += 1
            j += 1
    
    resultado_idx.extend(arr_izq)
    resultado_idx.extend(arr_der)

    return resultado_ranking, resultado_idx

def superados(ranking,ini,fin):
    if ini >= fin:
        return [ranking[ini]], [0]
    
    mid = (ini + fin) // 2

    arr_izq, idx_izq = superados(ranking,ini,mid)
    arr_der, idx_der = superados(ranking,mid+1,fin)

    return merge(idx_izq,idx_der,arr_izq,arr_der)


arr = [('A',3),('B',4),('C',2),('D',8),('E',6),('F',5)]
print(superados(arr,0,len(arr)-1))