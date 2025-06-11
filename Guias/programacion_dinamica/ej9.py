
def max_estaciones(estaciones,n):
    OPT = [[float('-inf')]*3 for _ in range(n+1)]

    OPT[0][0] = 0
    OPT[1][0] = 0
    OPT[1][1] = estaciones[0]

    for i in range(2,n+1):
        OPT[i][0] = max(OPT[i-1][0],OPT[i-1][1],OPT[i-1][2])
        OPT[i][1] = OPT[i-1][0] + estaciones[i-1]
        OPT[i][2] = OPT[i-1][1] + estaciones[i-1]

    return max(OPT[n])