import math

def mismo_punto(a,b):
    return a[0] - b[0] == 0 and a[1] - b[1] == 0

def distancia_euclidiana(a,b):
    return math.dist(a,b)

def par_ya_incluido(a,b,arr):
    for par in arr:
        if a == par[0] and b == par[1]:
            return True
        
        if a == par[1] and b == par[0]:
            return True
    return False

def crear_par(a,b):
    return (a,b)


def puntos_cercanos_bt(i,puntos,sum_act,sum_min,act_p,min_p):
    if len(act_p) == 3:
        if sum_act < sum_min[0]:
            min_p.clear()
            min_p.extend(act_p.copy()) 
            sum_min[0] = sum_act
        return
    
    if i >= len(puntos):
        return

    actual = puntos[i]

    for punto in puntos:
        if mismo_punto(actual,punto):
            continue

        if par_ya_incluido(actual,punto,act_p):
            continue

        dist = distancia_euclidiana(actual,punto)
        sum_act += dist
        i += 1
        act_p.append(crear_par(actual,punto))
        puntos_cercanos_bt(i,puntos,sum_act,sum_min,act_p,min_p)
        sum_act -= dist
        i -= 1
        act_p.pop()

    puntos_cercanos_bt(i+1,puntos,sum_act,sum_min,act_p,min_p)
    i -= 1

P = [(1,2),(3,4),(5,6),(7,8),(9,10)]
sum_min = [float('inf')]  # Inicializar con infinito
min_p = []  # Aquí se guardarán los 3 pares más cercanos

puntos_cercanos_bt(0, P, 0, sum_min, [], min_p)
print("Pares más cercanos:", min_p)
print("Suma de distancias:", sum_min[0])

