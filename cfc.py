from grafo import Grafo

class CompFortConexas:
    def __init__(self, grafo):
        self.grafo = grafo
        self.componentes = []
        self.tempo = 0
        self.executar()
        self.matrizDFS = [[False, float('infinite'), float('infinite'), None] for i in range(self.grafo.qtdVertices())]
        

    def DFSVisit(self, k, tempo):
        self.matrizDFS[k][0] = True
        self.tempo += 1
        self.matrizDFS[k][1] = self.tempo

        for m in range(len(self.grafo.vizinhos())):
            if self.matrizDFS[m][0] == False:
                self.matrizDFS[m][3] = k
                self.DFSVisit(m)

        self.tempo += 1
        self.matrizDFS[k] = self.tempo


    def DFS(self):
        for i in range(self.grafo.qtdVertices()):
            # matrizDFS[i] = Cv, Tv, Fv, Av
            self.matrizDFS[i] = [False, float('infinite'), float('infinite'), None]

        self.tempo = 0

        for k in range(self.grafo.qtdVertices()):
            if self.matrizDFS[k][0] == False:
                self.DFSVisit(k)

    def executar(self):
        self.DFS()
        #Criar o grafo transposto
        arestasTransp = []

        for aresta in self.grafo.arestas:
            arestasTransp.append([aresta.vertices[1], aresta.vertices[0]])