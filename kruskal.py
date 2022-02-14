from grafo import Grafo

def kruskal(grafo):
    A = set()
    S = [None for i in range(grafo.qtdVertices()+1)]

    for v in grafo.vertices:
        S[v.index] = {v}

    E = grafo.arestas
    sorted_E = []
    K = {}
    for i in range(grafo.qtdArestas()):
        K[E[i]] = E[i].peso
    K_sorted = sorted(K.items(), key=lambda item: item[1])
    for k in K_sorted.keys():
        sorted_E.append(k)

    for aresta in sorted_E:
        a, b = aresta.vertices


g = Grafo()
g.ler("entradas/kruskal.txt")
kruskal(g)