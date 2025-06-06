import networkx as nx

def camino_minimo(grado,nodo_or,nodo_ds):
    return

"""
terminar de implementar
"""


if __name__ == "__main__":
    grafo = nx.Graph

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