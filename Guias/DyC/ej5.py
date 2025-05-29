def mas_de_la_mitad(lote,ini,fin):
    if ini >= fin:
        return lote[ini],lote[ini:fin+1],1
    
    mid = (ini + fin) // 2

    cand_izq, arr_izq, cant_izq = mas_de_la_mitad(lote,ini,mid)
    cand_der, arr_der, cant_der = mas_de_la_mitad(lote,mid+1,fin)

    return merge(arr_izq,arr_der,cand_izq,cand_der,cant_izq,cant_der)

def merge(arr_izq,arr_der,candidato_izq,candidato_der,cant_izq,cant_der):
    resultado = []
    resultado.extend(arr_izq)
    resultado.extend(arr_der)

    i = j = 0 

    if candidato_izq == candidato_der:
        return candidato_izq, resultado, cant_izq + cant_der
         

    while i < len(arr_der) and j < len(arr_izq):
        if arr_der[i] == candidato_izq:
            cant_izq += 1
        
        if arr_izq[j] == candidato_der:
            cant_der += 1
        
        i += 1
        j += 1
    
    while i < len(arr_der):
        if arr_der[i] == candidato_izq:
            cant_izq += 1
        
        i+=1

    while j < len(arr_izq):
        if arr_izq[j] == candidato_der:
            cant_der += 1
        
        j+=1
    
    if cant_izq > cant_der and cant_izq > len(resultado) // 2:
        return candidato_izq, resultado, cant_izq
    elif cant_der > cant_izq and cant_der > len(resultado) // 2:
        return candidato_der, resultado, cant_izq
    else:
        return None, resultado, 0


arr = [6, 6, 1, 1, 2, 2]
print(mas_de_la_mitad(arr,0,len(arr)-1))

    


    