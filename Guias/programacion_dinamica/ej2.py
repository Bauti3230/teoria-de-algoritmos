import networkx as nx
"""
Tenemos un grafo dirigido, aciclio con pesos entre sus aristas y dos
vertices 's' y 't'. Queremos encontrar el camino de mayor peso entre
's' y 't'.

Analisis : 
    Como el grafo es asiclico nos permite usar un orden topologico

    def orden topologico : 
        Un ordenamiento topologico es una dispocision lineal de nodos 
        de un grafo asicilico dirigido, donde el nodo aparece antes 
        que a todos lo que apunta.
"""

def orden_topologico(grafo,nodos):
    visitados = set()
    pila = []

    for nodo in nodos:
        if nodo not in visitados:
            orden_topologico_rec(grafo,nodo,pila,visitados)
    return pila[::-1]

def orden_topologico_rec(grafo,nodo,pila,visitados):
    visitados.add(nodo)
    for nodo_adyacente in list(grafo.adj[nodo]):
        if nodo_adyacente not in visitados:
            orden_topologico_rec(grafo,nodo_adyacente,pila,visitados)
    pila.append(nodo)



def max_camino_pesado(grafo,s,t):
    nodos = list(grafo.nodes)
    n = len(nodos)

    OPT = {}
    for nodo in nodos:
        value = float('-inf') if nodo != s else 0
        OPT.update({nodo:value})

    orden = orden_topologico(grafo,nodos)

    for nodo in orden:
        anterior = OPT[nodo]
        if anterior == float('-inf'):
            continue

        for nodo_ady in list(grafo.adj[nodo]):
            siguiente = anterior + grafo[nodo][nodo_ady]["weight"]
            if siguiente > OPT[nodo_ady]:
                OPT[nodo_ady] = siguiente

    return OPT[t]

if __name__ == "__main__":

    grafo = nx.DiGraph()
    nodos = ['A','B','C','D','E']
    
    grafo.add_nodes_from(nodos)
    grafo.add_edge('A', 'B', weight=4)  
    grafo.add_edge('A', 'C', weight=2)  
    grafo.add_edge('B', 'D', weight=5)  
    grafo.add_edge('C', 'D', weight=1)  
    grafo.add_edge('C', 'E', weight=3)  
    grafo.add_edge('D', 'E', weight=2)
    
    max_camino_pesado(grafo,'A','E')


