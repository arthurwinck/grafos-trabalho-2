from cfc import CompFortConexas
from grafo import Grafo

grafo1 = Grafo()
grafo1.ler('entradas/cfc2.txt')

cfc = CompFortConexas(grafo1)