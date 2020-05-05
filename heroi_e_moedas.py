from lib.grafo import Grafo
from lib.arvore import Arvore
from colorama import Fore, init as color

color()

grafo = Grafo.get_grafo("heroi_e_moedas")

vertice_origem = "1"
moedas = ["5", "9", "12", "15", "16", "18", "21", "25", "28"]

pilha = [vertice_origem]
vertices_visitados = Arvore(vertice_origem)

while pilha and moedas:
    vertice = pilha[-1]
    explorado = True
    for w in grafo.get_adjacentes(vertice):
        if not vertices_visitados.localizar_nodo(w):
            explorado = False
            break
    if explorado:
        pilha.pop(-1)
    for w in grafo.get_adjacentes(vertice):
        if not vertices_visitados.localizar_nodo(w):
            vertices_visitados.inserir_nodo(vertice, w)
            if w in moedas:
                moedas.remove(w)
            pilha.append(w)
            break

vertices_visitados.imprimir()

print(f"{Fore.YELLOW}\nENTER para finalizar{Fore.RESET}")
input()
