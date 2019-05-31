from . import dijkstra

def centralidad(grafo):
    """Mediante Betweeness Centrality genera un vector con los vertices ordenados
    por importancia"""

    centralidad={}
    for vertice in grafo:
        centralidad[vertice]=0

    for vertice in grafo:
        centralidad_auxiliar= {}
        distancia,predecesor= dijkstra.dijkstra(grafo,vertice)

        for w in grafo:
            centralidad_auxiliar[w]=0

        distancias_filtradas= {k: v for k, v in distancia.items() if v<float("inf")}

        for w in sorted(distancias_filtradas, key=distancias_filtradas.__getitem__,reverse=True):
            if w==vertice: continue
            centralidad_auxiliar[predecesor[w]]+=1
            centralidad_auxiliar[predecesor[w]]+=centralidad_auxiliar[w]

        for w in grafo:
            if w==vertice: continue
            centralidad[w]+=centralidad_auxiliar[w]

    return centralidad
