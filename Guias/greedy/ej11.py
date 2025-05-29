def ocupar_adyacntes(tablero, i, j):
    for i_idx in -1, 0, 1:
        for j_idx in -1, 0,1:

            if i_idx == 0 and j_idx == 0:
                continue

            if i + i_idx < 0 or i + i_idx > len(tablero) or j + j_idx < 0 or j + j_idx > len(tablero[i]):
                continue

            tablero[i+i_idx][j+j_idx] = 1

def ordenar_reyes(n,m):
    tablero = [[0 for col in range(m)]for row in range(n)]

    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == 0:
                tablero[i][j] = 'R'
                ocupar_adyacntes(tablero ,i,j)
    
    return tablero

tablero_final = ordenar_reyes(8,8)
print(tablero_final)