import networkx as nx
from collections import deque

def edmonds_karp(G, source, sink):
    G_residual = G.copy()
    flujo_dict = {u: {v: 0 for v in G[u]} for u in G.nodes}
    
    for u in G.nodes:
        for v in G.nodes:
            if v not in flujo_dict[u]:
                flujo_dict[u][v] = 0
    
    def bfs(s, t):
        padres = {s: None}
        capacidades = {s: float('inf')}
        cola = deque([s])
        
        while cola:
            u = cola.popleft()
            for v in G_residual[u]:
                residual = G_residual[u][v].get('weight', 0) - flujo_dict[u][v]
                if v not in padres and residual > 0:
                    padres[v] = u
                    capacidades[v] = min(capacidades[u], residual)
                    if v == t:
                        return capacidades[t], padres
                    cola.append(v)
        return 0, {}
    
    flujo_maximo = 0
    while True:
        capacidad, padres = bfs(source, sink)
        if capacidad == 0:
            break
        flujo_maximo += capacidad
        v = sink
        while v != source:
            u = padres[v]
            flujo_dict[u][v] += capacidad
            flujo_dict[v][u] = -flujo_dict[u][v]
            v = u
    
    return flujo_maximo, flujo_dict

def agregar_nodo(grafo,nodo,dic_pred,res):

    nodos_pred = dic_pred[nodo]
    
    if nodo == "s" or nodo == "x":
        grafo.add_node(nodo)

        for pred in nodos_pred:
            grafo.add_edge(pred,nodo,weight=res)
        return
    
    nodo_prim = nodo + "'"   
    grafo.add_node(nodo_prim)
    
    for pred in nodos_pred:
        grafo.add_edge(pred,nodo_prim,weight=float('inf'))
    grafo.add_node(nodo)
    grafo.add_edge(nodo_prim,nodo,weight=res)

    return

def crear_grafo_transporte(dic_planetas,dic_pred):
    grafo = nx.DiGraph()
    for planeta, resticcion in dic_planetas.items():
        agregar_nodo(grafo,planeta,dic_pred,resticcion)
    return grafo

if __name__ == "__main__":
    
    dic_planetas = {
        "s" : float('inf'),
        "A" : 10,
        "B" : 15,
        "C" : 8 ,
        "x" : float('inf')
    }

    dic_pred = {
        "s" : [],
        "A" : ["s"],
        "B" : ["s","A"],
        "C" : ["A","B"],
        "x" : ["C"]
    }
    
    grafo = crear_grafo_transporte(dic_planetas,dic_pred)

    print(edmonds_karp(grafo,"s","x")) 