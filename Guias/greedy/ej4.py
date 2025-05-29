

"""
tenemos "m" salas para dar "n" charlas. queremos minimizar la cantidad 
de salas utilizadas, o sea si podemos ordenar todas las charlas para 
que entren en una sola sala lo hacemos.
cada charla tiene un horario de inicio y de finalizacion (ini, fin).
tambien queremos que las charlas tengan un intervalo de 15 min entre charlas.
"""
def asignar_charlas(charlas,n):
    charlas.sort(key=lambda x:x[1])
    salas = []
    colocada = False

    for charla in charlas:

        colocada = False

        for charla_sala in salas :
            if charla_sala[-1][1] + 15 > charla[0]:
                continue

            charla_sala.append(charla)
            colocada = True
            break

        if not colocada and len(salas)+1 <= n:
            salas.append([charla])
            colocada = True
            continue
        
        if not colocada and len(salas) == n:
            return None, -1
    
    return salas, len(salas)

if __name__ == "__main__":
    charlas = [(60, 90), (90, 120), (120, 150)]
    m = 1

    salas, n = asignar_charlas(charlas,m)

    print(salas)
