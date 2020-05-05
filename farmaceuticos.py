from lib.grafo import Grafo
from colorama import Fore, init as color

color()

grafo = Grafo.get_grafo("farmaceuticos")

vertices_nao_coloridos = grafo._vertices
cores = [[]]

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

for idx, cor in enumerate(cores):
    print(f"{Fore.YELLOW}COR {idx + 1}:{Fore.RESET} {cor}")

print(f"{Fore.YELLOW}\nENTER para finalizar{Fore.RESET}")
input()
