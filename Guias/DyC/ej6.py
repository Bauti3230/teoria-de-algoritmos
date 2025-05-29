
"""
tenemos un lista de 'n' coords tal que (x,y) que forman un 
area poligonal convexa.
queremos mostrar ese sector del mapa con el mayor tamanio posibles.
el programa recibe como parametros dos coords para construir el rectangulo.
Construlla un algoritmo que los resuelva en O(log n)
"""

def coords_pantalla(coords,ini,fin):
    if fin - ini <= 3:
        aux = None
        for i in range(ini,fin+1):
            if aux is None or aux[1] < coords[i][1]:
                aux = coords[i]
        return aux

        return """devolvemos el maximo"""
    
    mid = (ini + fin) // 2

    ini_coord = coords[ini]
    mid_coord = coords[mid]
    
    if coords[ini+1][1] - ini_coord[1] >= 0:
        if coords[mid+1][1] - mid_coord[1] < 0:
            return coords_pantalla(coords_pantalla,ini,mid)
        
        if mid_coord[1] > ini_coord[1]:
            return coords_pantalla(coords,mid,fin)
    
        return coords_pantalla(coords,ini,mid)
    
    if coords[mid+1][1] - mid_coord > 0:
        return coords_pantalla(coords,mid,fin)
    
    if coords[mid+1] - mid_coord < 0 and mid_coord[1] < ini_coord[1]:
        return coords_pantalla(coords,mid,fin)
    
    return coords_pantalla(coords,ini,mid)

coords = [(0,0),(2,0),(3,2),(1,4),(-1,2)]

print(coords_pantalla(coords,0,len(coords)-1))
    



