from random import shuffle
from lib.grafo import Grafo
from colorama import Fore, init as color

color()

grafo = Grafo.retorna_grafo("sudoku")


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


print(
    f"{Fore.YELLOW} A proposta é utilizar coloração para encontrar a "
    f"resposta de um jogo de sudoku 4x4. Sabendo que o número de 'cores' não "
    f"poderia ser maior que 4, o algoritmo foi repetido até encontar este "
    f"resultado.{Fore.RESET}\n")

lista_cores = colorir(grafo)
while len(lista_cores) > 4:
    for idx, cor in enumerate(lista_cores):
        print(f"{Fore.YELLOW}COR {idx + 1}:{Fore.RESET} {cor}")
    print(f"{Fore.YELLOW}\nComo a lista gerada possui mais de 4 'cores', a "
          f"lista de vértices do grafo é embaralhada, e o processo de "
          f"coloração executado novamente. Este processo se repete até que "
          f"tenhamos uma solução satisfatória.\n{Fore.RESET}")
    input()
    shuffle(grafo._vertices)
    lista_cores = colorir(grafo)

for idx, cor in enumerate(lista_cores):
    print(f"{Fore.MAGENTA}COR {idx + 1}:{Fore.RESET} {cor}")
print(f"{Fore.MAGENTA}\nFinalmente gerada a lista de quatro cores, finaliza-se "
      f"o nosso algoritmo.{Fore.RESET} ")

print(f"{Fore.YELLOW}\nENTER para finalizar{Fore.RESET}")
input()
