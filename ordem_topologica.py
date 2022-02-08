from grafo import Grafo

def ordenacao_topologica(grafo):
    qtdVertices = grafo.qtdVertices()
    c = [False] * (qtdVertices + 1)
    ordem = []
    # tempo = 0

    for i in grafo.getVertices():
        if (c[i] == False):
            dfs_visit_ot(grafo, i, c, ordem)

    for j, i in enumerate(ordem):
        print(grafo.rotulo(i), end='')
        if j < len(ordem) - 1:
            print(' > ', end='')
    print()


def dfs_visit_ot(grafo, i, c, ordem):
    c[i] = True
    # tempo = tempo + 1
    vizinhos = grafo.vizinhos(i)
    for j in vizinhos(i):
        if (c[i] == False):
            dfs_visit_ot(grafo, i, c, ordem)

    ordem.append(i)

grafo1 = Grafo()
grafo1.ler('entradas/teste.txt')