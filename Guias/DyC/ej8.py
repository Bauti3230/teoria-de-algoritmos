def cubrir_patio(n, sumidero):
    # Creamos una matriz n x n inicializada a 0
    patio = [[0 for _ in range(n)] for _ in range(n)]
    # Marcamos el sumidero con -1
    patio[sumidero[0]][sumidero[1]] = -1
    # Llamamos a la función recursiva
    colocar_baldosas(patio, 0, 0, n, sumidero)
    return patio

def colocar_baldosas(patio, fila, col, tamaño, sumidero):
    if tamaño == 2:
        # Caso base: colocar una baldosa en L
        baldosa = 1
        for i in range(fila, fila+2):
            for j in range(col, col+2):
                if patio[i][j] == 0:  # Si no es el sumidero
                    patio[i][j] = baldosa
        return baldosa + 1
    
    mitad = tamaño // 2
    # Determinar en qué cuadrante está el sumidero
    cuadrante = 0
    if sumidero[0] >= fila + mitad:
        if sumidero[1] >= col + mitad:
            cuadrante = 3  # Abajo derecha
        else:
            cuadrante = 2  # Abajo izquierda
    else:
        if sumidero[1] >= col + mitad:
            cuadrante = 1  # Arriba derecha
        else:
            cuadrante = 0  # Arriba izquierda
    
    # Colocar baldosa en L en el centro, evitando el cuadrante con el sumidero
    pos_centro = [(fila+mitad-1, col+mitad-1), (fila+mitad-1, col+mitad),
                 (fila+mitad, col+mitad-1), (fila+mitad, col+mitad)]
    
    baldosa_actual = tamaño * tamaño // 3  # Identificador único para la baldosa
    
    for i in range(4):
        if i != cuadrante:
            x, y = pos_centro[i]
            patio[x][y] = baldosa_actual
    
    # Resolver recursivamente cada cuadrante
    nuevos_sumideros = [
        (fila+mitad-1, col+mitad-1), (fila+mitad-1, col+mitad),
        (fila+mitad, col+mitad-1), (fila+mitad, col+mitad)
    ]
    
    # Cuadrante superior izquierdo
    if cuadrante == 0:
        s = sumidero
    else:
        s = nuevos_sumideros[0]
    colocar_baldosas(patio, fila, col, mitad, s)
    
    # Cuadrante superior derecho
    if cuadrante == 1:
        s = sumidero
    else:
        s = nuevos_sumideros[1]
    colocar_baldosas(patio, fila, col+mitad, mitad, s)
    
    # Cuadrante inferior izquierdo
    if cuadrante == 2:
        s = sumidero
    else:
        s = nuevos_sumideros[2]
    colocar_baldosas(patio, fila+mitad, col, mitad, s)
    
    # Cuadrante inferior derecho
    if cuadrante == 3:
        s = sumidero
    else:
        s = nuevos_sumideros[3]
    colocar_baldosas(patio, fila+mitad, col+mitad, mitad, s)
    
    return baldosa_actual + 1

# Ejemplo de uso para un patio 4x4 con sumidero en (2,1)
patio = cubrir_patio(4, (2,1))
for fila in patio:
    print(fila)