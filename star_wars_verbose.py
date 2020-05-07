from lib.grafo import Grafo
from lib.arvore import Arvore
from colorama import Fore, init as color

color()

print(
    f"{Fore.YELLOW} Proprosta: A partir da busca em largura em uma árvore "
    f"genealógica, encontrar o grau de parentesco entre o Mestre Yoda e a "
    f"Princesa Leia Organa. {Fore.RESET}")
print(f"\nVértice Origem: YODA")
print(f"Vértice Destino: PRINCESS LEIA ORGANA")
input()

grafo = Grafo.retorna_grafo("star_wars")

vertice_origem = "YODA"

vertice_destino = "PRINCESS LEIA ORGANA"

fila = [vertice_origem]
vertices_visitados = Arvore(vertice_origem)

print(
    f"{Fore.YELLOW}Para dar inicio ao algoritmo, adicionamos o vértice de "
    f"origem à fila e "
    f"à Árvore de vértices visitados. Temos: {Fore.RESET}")
print(f"FILA: {fila}")
print(f"VÉTICES VISITADOS:")
vertices_visitados.imprimir()
input()

while fila:
    if vertices_visitados.localizar_nodo(vertice_destino):
        break
    vertice = fila[0]
    fila.pop(0)
    for w in grafo.get_adjacentes(vertice):
        if not vertices_visitados.localizar_nodo(w):
            vertices_visitados.inserir_nodo(vertice, w)
            fila.append(w)
    print()
    print(
        f"\n{Fore.YELLOW}Os vértices adjacentes ao primeiro vértice da Fila "
        f"são adicionados à Fila, enquanto ele, uma vez explorado, "
        f"é removido. Temos:{Fore.RESET}")
    print(f"FILA: {fila}")
    print(f"VÉTICES VISITADOS:")
    vertices_visitados.imprimir()
    input()

print(f"\n{Fore.YELLOW}A fila ainda não está vazia, mas como o vértice destino já está "
      f"explorado, podemos parar a execução por aqui. Resultado Final:")
print(f"Pela arvore gerada, é possível notar que {Fore.MAGENTA}o grau de "
      f"parentesco do mestre Yoda com a princesa Leia é 2.{Fore.RESET}")

print(f"{Fore.YELLOW}\nENTER para finalizar{Fore.RESET}")
input()
