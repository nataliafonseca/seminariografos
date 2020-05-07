from lib.grafo import Grafo
from colorama import Fore, init as color

color()

grafo = Grafo.retorna_grafo("superman")

print(
    f"{Fore.YELLOW} A proposta é utilizar ordenação topológica para obter a "
    f"ordem em que as roupas do superman devem ser vestidas.{Fore.RESET}\n")

lista_de_listas = []
while grafo._vertices:
    graus_entrada_por_vertice = {}
    for vertice in grafo._vertices:
        graus_entrada_por_vertice[vertice] = \
            grafo.obter_grau_de_entrada(vertice)
    lista_de_saida = []
    for vertice, grau_de_entrada in graus_entrada_por_vertice.items():
        if grau_de_entrada == 0:
            lista_de_saida.append(vertice)
            grafo.remover_do_grafo(vertice)
    lista_de_listas.append(lista_de_saida)

for idx, lista in enumerate(lista_de_listas):
    print(f"{Fore.YELLOW}ETAPA {idx + 1}:{Fore.RESET} {lista}")

print(f"{Fore.YELLOW}\nENTER para finalizar{Fore.RESET}")
input()
