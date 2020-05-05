from lib.grafo import Grafo
from lib.arvore import Arvore
from colorama import Fore, init as color

color()

grafo = Grafo.get_grafo("star_wars")

vertice_origem = "YODA"
vertice_destino = "PRINCESS LEIA ORGANA"

fila = [vertice_origem]
vertices_visitados = Arvore(vertice_origem)

while fila:
    if vertices_visitados.localizar_nodo(vertice_destino):
        break
    vertice = fila[0]
    fila.pop(0)
    for w in grafo.get_adjacentes(vertice):
        if not vertices_visitados.localizar_nodo(w):
            vertices_visitados.inserir_nodo(vertice, w)
            fila.append(w)

vertices_visitados.imprimir()

print(f"{Fore.YELLOW}\nENTER para finalizar{Fore.RESET}")
input()
