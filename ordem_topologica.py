from grafo import Grafo, Vertice

def ordenacao_topologica(grafo):
    ordem = []
    c = [False] * (grafo.qtdVertices())

    for i in range(grafo.qtdVertices()):
        if c[i] == False:
            dfs_visit_ot(grafo,i,c,ordem)
    
    new_ordem = []
    ordem.pop()
    ordem = [int(x-1) for x in ordem]

    for k in ordem:
        vertice = grafo.vertices[k]
        new_ordem.append(grafo.rotulo(vertice))
    
    for x in range(len(new_ordem)):
        new_ordem[x] = (' '.join(new_ordem[x]))
    
    print(" -> ".join(new_ordem))

def dfs_visit_ot(grafo,i,c,ordem):
    c[i] = True
    vizinhos = grafo.vizinhos(i+1)
    for j in vizinhos:
        if c[j-1] == False:
            c, ordem = dfs_visit_ot(grafo,j-1,c,ordem)
    
    ordem.insert(0,i)
    return (c,ordem)

grafo1 = Grafo()

grafo1.ler('entradas/teste.txt')

ordenacao = ordenacao_topologica(grafo1)