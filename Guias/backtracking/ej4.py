def camino_hamiltoniano_caballo(tablero, visitados, i, j):
    if len(visitados) == 64:
        # Verificar si puede volver al inicio (0, 0)
        movimientos_finales = movimientos_caballo(i, j)
        if (0, 0) in movimientos_finales:
            return True
        else:
            return False
    
    movimientos = movimientos_caballo(i, j)
    for ni, nj in movimientos:
        if not tablero[ni][nj]:
            tablero[ni][nj] = True
            visitados.append((ni, nj))
            
            if camino_hamiltoniano_caballo(tablero, visitados, ni, nj):
                return True
            
            # Backtracking
            tablero[ni][nj] = False
            visitados.pop()
    
    return False

def movimientos_caballo(i, j):
    movimientos = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2),  (1, 2),
        (2, -1),  (2, 1)
    ]
    posibles = []
    for di, dj in movimientos:
        ni, nj = i + di, j + dj
        if 0 <= ni < 8 and 0 <= nj < 8:
            posibles.append((ni, nj))
    return posibles

# Inicialización
tablero = [[False for _ in range(8)] for _ in range(8)]
i_inicial, j_inicial = 0, 0
tablero[i_inicial][j_inicial] = True
visitados = [(i_inicial, j_inicial)]

# Ejecución
if camino_hamiltoniano_caballo(tablero, visitados, i_inicial, j_inicial):
    print("¡Se encontró un ciclo hamiltoniano!")
    print("Camino:", visitados)
else:
    print("No se encontró un ciclo hamiltoniano.")