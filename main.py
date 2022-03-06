from cfc import CompFortConexas
from grafo import Grafo

grafo1 = Grafo()
grafo1.ler('entradas/dirigido1.net')

cfc = CompFortConexas(grafo1)
