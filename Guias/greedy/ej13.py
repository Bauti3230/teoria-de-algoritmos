import networkx as nx

def no_visitado(nodo,solucion):
    for camino in solucion:
        if camino in solucion : return False
    return True 

"""
queremos que un centro de distribucion de repuesto le lleve a cada estacion repuestos
y querempo maximizar la cantidad de repuestos que puede llevar.
podemos armar mas de un camino entonces, pero no podemos revisitar estaciones por las 
que ya pasamos
"""
def centro_de_dsitrubucion(grafo):

    nodos = list(grafo.nodes())
    index_cd = nodos.index('Centro')
    solucion = []

    nodo_act = nodos[index_cd]
    i = 0
    
    
    aux = []

    for nodo_ady in sorted(grafo.adj[nodo_act], reverse=True):
        solucion_actual = []
        
        if nodo_act == 'Centro' :
            solucion_actual.append(nodo_act)

        if no_visitado(nodo_ady,solucion) and nodo_ady not in solucion_actual:
            solucion_actual.append(nodo_ady)
            nodo_act = nodo_ady
            aux += solucion_actual
            continue



    return

if __name__ == "__main__":
    grafo = nx.Graph()
    
    nodos = ['Centro', 'Est1', 'Est2', 'Est3', 'Est4', 'Est5']
    grafo.add_nodes_from(nodos)

    aristas = [
    ('Centro', 'Est1', 10),
    ('Centro', 'Est2', 15),
    ('Est1', 'Est3', 5),
    ('Est2', 'Est3', 12),
    ('Est2', 'Est4', 8),
    ('Est3', 'Est5', 6),
    ('Est4', 'Est5', 7)
    ]

    for u, v, w in aristas:
        grafo.add_edge(u, v, weight=w)

    centro_de_dsitrubucion(grafo)
    