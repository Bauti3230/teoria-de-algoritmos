
"""
tenemos un arreglo que nos dice cuanta ganancia tendriamos por comprar un terreno.
cada indice del arreglo representa una ganancia o perdida.
nosotros queremos ver que terrenos contiguos comprar para MAXIMIZAR la ganancia.

basicamente nene esto es una maxima sumatoria seguida:

S = [-2, 3, -3, 4, -1, 2]
"""
def terrenos_contiguos(terrenos):
    n = len(terrenos)
    
    OPT = [0] * n
    reco = [0] * n

    OPT[0] = terrenos[0]
    reco[0] = -1

    for i in range(1,n):
        OPT[i] = max(terrenos[i],OPT[i-1] + terrenos[i])

        if terrenos[i] >= OPT[i-1] + terrenos[i]:
            reco[i] = -1
        else :
            reco[i] = i-1

    return OPT[n-1],reco

S = [-2, 3, -3, 4, -1, 2]
print(terrenos_contiguos(S))


