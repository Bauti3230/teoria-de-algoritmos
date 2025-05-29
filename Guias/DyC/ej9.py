
"""
voy a usar una tecnica re LOL llamada arreglo virtual ordenado
y como hacemos esto loquitooo, bueno definimos un inicio, un
final y una matriz que debe seguir un orden.
el orden que la matriz debe seguir es que los elementos en las filas
deben estar ordenados [1,2,3,...,etc] pero aparte el resto de filas 
deben ser mayores (o menore) [2,3,4,...,etc] : 
    [1,4,7]
    [2,5,8]
    [3,6,9]
como se ve en este ejemplo re trivial tanto las filas como columnas 
estan ordenadas.
"""
def busqueda_binaria_matriz(matriz,ini,fin,n,buscado):
    if ini > fin:
        return None
    
    mid = (ini+fin) // 2

    i = mid // n
    j = mid % n

    elemento = matriz[i][j]

    if elemento == buscado:
        return i,j
    
    if elemento > buscado:
        return busqueda_binaria_matriz(matriz,ini,mid-1,n,buscado)
    
    return busqueda_binaria_matriz(matriz,mid+1,fin,n,buscado)

M = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 13],
    [10, 14, 15, 16]
]
target = 9
busqueda_binaria_matriz(M,0,len(M) * len(M[0]) - 1,len(M[0])-1,target)