from grafo import Grafo, Vertice

def ordenacao_topologica(grafo):
    ordem = []
    c = [False] * (grafo.qtdVertices())

    for i in range(grafo.qtdVertices()):
        if c[i] == False:
            c, ordem = dfs_visit_ot(grafo,i,c,ordem)
    
    new_ordem = []
    ordem = [int(x) for x in ordem]

    for k in ordem:
        vertice = grafo.vertices[k-1]
        new_ordem.append(grafo.rotulo(vertice))

    
    for i in range(len(new_ordem)-1):
        new_ordem[i] = new_ordem[i] + " -> "

    print(''.join(new_ordem))

def dfs_visit_ot(grafo,i,c,ordem):
    c[i] = True
    lista_vizinhos = []       
    vizinhos = grafo.vizinhos(i+1)

    for l in range(len(grafo.arestas)):
        if grafo.arestas[l].vertices[0] == i+1:
            lista_vizinhos.append(grafo.arestas[l].vertices[1] - 1)

    for j in lista_vizinhos:
        if c[j] == False:
            c, ordem = dfs_visit_ot(grafo,j,c,ordem)
            
    ordem.insert(0,i+1)
    return (c,ordem)

grafo1 = Grafo()

grafo1.ler('entradas/topological.net')

ordenacao = ordenacao_topologica(grafo1)