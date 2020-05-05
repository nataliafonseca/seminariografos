from random import shuffle
from lib.grafo import Grafo
from colorama import Fore, init as color

color()

grafo = Grafo.get_grafo("sudoku")


def colorir(grafo):
    vertices_nao_coloridos = grafo._vertices

    cores = [["v1", "v10"], ["v7"], ["v16"], []]

    for vertice in vertices_nao_coloridos:
        ha_adjacente = False
        for idx, cor in enumerate(cores):
            ha_adjacente = False
            if vertice in cores[idx]:
                break
            for adjacente in grafo.get_adjacentes(vertice):
                if adjacente in cores[idx]:
                    ha_adjacente = True
                    break
            if not ha_adjacente:
                cor.append(vertice)
                break
        if ha_adjacente:
            cores.append([vertice])

    return cores


lista_cores = colorir(grafo)
while len(lista_cores) > 4:
    shuffle(grafo._vertices)
    lista_cores = colorir(grafo)

for idx, cor in enumerate(lista_cores):
    print(f"{Fore.YELLOW}COR {idx + 1}:{Fore.RESET} {cor}")

print(f"{Fore.YELLOW}\nENTER para finalizar{Fore.RESET}")
input()
