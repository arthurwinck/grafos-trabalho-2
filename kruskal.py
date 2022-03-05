from grafo import Grafo

def print_vector(A):
    for a in A:
        print(a)

def unir(A,  B):
    x = []
    for a in A:
        x.append(a)
    for b in B:
        x.append(b)
    return x

def kruskal(grafo):
    A = set()
    S = [None for i in range(grafo.qtdVertices()+1)]

    for v in grafo.vertices:
        S[v.index] = {v}

    E = grafo.arestas
    print_vector(E)
    print('')
    sorted_E = []
    K = {}
    for i in range(grafo.qtdArestas()):
        K[E[i]] = E[i].peso
    K_sorted = sorted(K.items(), key=lambda item: item[1])
    for k in K_sorted:
        sorted_E.append(k[0])
    print_vector(sorted_E)

    for aresta in sorted_E:
        u, v = aresta.vertices
        if S[u] != S[v]:
            A.add((u, v))
            x = unir(S[u], S[v])
            for y in x:
                S[y.index] = x

    return A

g = Grafo()
g.ler("entradas/kruskal.txt")
print(kruskal(g))