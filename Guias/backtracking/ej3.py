"""
el problema de las n reinas basicamente es colocar n reinas en un tablero de 
"""

def pos_no_conflict(ocupado,i,j):
    pos = (i,j)
    return pos in ocupado

def marcar_casillas_atacadas(tablero, i, j):
    n = len(tablero)
    modificadas = []  
    
    direcciones = [
        (-1, 0), (1, 0), (0, -1), (0, 1),  
        (-1, -1), (-1, 1), (1, -1), (1, 1)  
    ]
    
    for di, dj in direcciones:
        ni, nj = i + di, j + dj
        while 0 <= ni < n and 0 <= nj < n:
            if tablero[ni][nj] == 0:  
                tablero[ni][nj] = -1
                modificadas.append((ni, nj))
            ni += di
            nj += dj
    
    return modificadas  

def desmarcar_casillas_atacadas(tablero, modificadas):
    for i, j in modificadas:
        tablero[i][j] = 0  

def n_reinas_bt(tablero,cant,j,n):
    if cant == n:
        return tablero
    
    if j >= n:
        return None
    
    for i in range(n):
        if tablero[i][j] == 0:
            tablero[i][j] = 1
            cant += 1
            mods = marcar_casillas_atacadas(tablero,i,j)
            sol = n_reinas_bt(tablero,cant,j+1,n)
            if sol: return sol
            tablero[i][j] = 0
            cant -= 1
            desmarcar_casillas_atacadas(tablero,mods)
    
    return None

def reinas_se_atacan(tablero):
    reinas = []
    n = len(tablero)
    
    # Paso 1: Recolectar posiciones de las reinas (1)
    for i in range(n):
        for j in range(n):
            if tablero[i][j] == 1:
                reinas.append((i, j))
    
    # Paso 2: Verificar si alguna reina ataca a otra
    for k in range(len(reinas)):
        i1, j1 = reinas[k]
        for l in range(k + 1, len(reinas)):
            i2, j2 = reinas[l]
            # Misma fila, columna o diagonal?
            if i1 == i2 or j1 == j2 or abs(i1 - i2) == abs(j1 - j2):
                return True  # ¡Hay al menos un ataque!
    
    return False  # No hay ataques
    
n = 4
tablero = [[0 for i in range(n)] for j in range(n)]

sol = n_reinas_bt(tablero,0,0,n)

if reinas_se_atacan(sol):
    print("¡Al menos una reina puede comer a otra!")
else:
    print("Ninguna reina se come a otra. ✅")