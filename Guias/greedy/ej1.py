"""
se recibe una arreblo de bifurcaciones de formato : 
    [(Castelli, 185), (Gral Guido, 249), ..., (Nombre, Km)]
devuelve la los lugares donde poner los patrulleros y la cantidad 
de patrulleros.
"""
def patrullas(bifurcaciones):
    bifurcaciones.sort(key=lambda x:x[1])
    solucion = []

    for bifurcacion in bifurcaciones :

        if len(solucion) == 0:
             solucion.append(bifurcacion)
             continue
    

        if bifurcacion[1] - solucion[-1][1] <= 50:
                continue

        solucion.append(bifurcacion)
        
        
    return solucion, len(solucion)

if __name__ == "__main__":
    bifurcaciones = [("Castelli", 185), ("Gral Guido", 249), ("Lezama", 156), ("Maipu", 270), ("Sevigne", 194)]

    solucion, n = patrullas(bifurcaciones)

    print(solucion)
    print(n)

