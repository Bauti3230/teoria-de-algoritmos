import networkx as nx

def asignaciones_medicos(grafo, s, t):
    grafo_residual = grafo.copy()
    flujo_dict = {u: {v: 0 for v in grafo[u]} for u in grafo.nodes()}
    
    for u in grafo.nodes:
        for v in grafo.nodes:
            if v not in flujo_dict[u]:
                flujo_dict[u][v] = 0
    
    def dfs(u, sumidero, flujo_min, visitados, padres):
        visitados.add(u)
        if u == sumidero:
            return flujo_min
        for v in grafo_residual[u]:
            residual = grafo_residual[u][v].get('weight', 0) - flujo_dict[u][v]
            if v not in visitados and residual > 0:
                padres[v] = u
                nuevo_flujo = dfs(v, sumidero, min(flujo_min, residual), visitados, padres)
                if nuevo_flujo > 0:
                    return nuevo_flujo
        return 0

    flujo_maximo = 0
    while True:
        padres = {}
        visitados = set()
        capacidad = dfs(s, t, float('inf'), visitados, padres)
        if capacidad == 0:
            break
        flujo_maximo += capacidad
        v = t  
        while v != s:
            u = padres[v]
            flujo_dict[u][v] += capacidad
            flujo_dict[v][u] = -flujo_dict[u][v]
            v = u
    
    return flujo_maximo, flujo_dict


def crear_grafo_medicos(medicos,periodos,F):
    
    grafo = nx.DiGraph()

    grafo.add_nodes_from(["s","t"])

    for medico, disp_periodo in medicos.items():
        grafo.add_node(medico)
        grafo.add_edge("s",medico,weight=F)
        
        for nam_periodo, dias in periodos.items():
            grafo.add_nodes_from(dias)
            
            nodo_periodo = nam_periodo + "_" + medico
            grafo.add_node(nodo_periodo)
            grafo.add_edge(medico,nodo_periodo,weight=1)

            dias_disp_periodo = disp_periodo[nam_periodo]
            for dia in dias_disp_periodo:
                grafo.add_edge(nodo_periodo,dia,weight=1)
                grafo.add_edge(dia,"t",weight=1)
    return grafo

def extraer_asignaciones(flujo_dict, medicos, periodos):
    asignaciones = {}
    for medico in medicos:
        for nom_periodo in periodos:
            nodo_periodo = f"{nom_periodo}_{medico}"
            for dia in periodos[nom_periodo]:
                if flujo_dict.get(nodo_periodo, {}).get(dia, 0) == 1:
                    asignaciones[dia] = medico
    return asignaciones

if __name__ == "__main__":
    medicos = {
        'A': {
            '9_de_julio': ['09/07', '10/07', '11/07', '12/07'],  # Disponible todos los días del período
            '1_de_mayo': ['01/05'],                              # Disponible el único día del período
            '25_de_mayo': ['25/05']                              # Disponible el único día del período
        },
        'B': {
            '9_de_julio': ['09/07', '11/07', '12/07'],           # Disponible en 3 días del período
            '1_de_mayo': [],                                     # No disponible
            '25_de_mayo': ['25/05']                              # Disponible
        },
        'C': {
            '9_de_julio': ['10/07', '12/07'],                    # Disponible en 2 días del período
            '1_de_mayo': ['01/05'],                              # Disponible
            '25_de_mayo': []                                     # No disponible
        }
    }

    periodos = {
        '9_de_julio': ['09/07', '10/07', '11/07', '12/07'],      # Período de 4 días
        '1_de_mayo': ['01/05'],                                  # Período de 1 día
        '25_de_mayo': ['25/05']                                  # Período de 1 día
    }

    F = 4
    grafo = crear_grafo_medicos(medicos,periodos,F)
    sucesores = list(grafo.successors("A"))
    print(sucesores)
    
    fulujo_max, fujo_dict = asignaciones_medicos(grafo,"s","t")

    asg = extraer_asignaciones(fujo_dict,medicos,periodos)

    print(asg)