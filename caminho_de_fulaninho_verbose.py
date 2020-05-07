from copy import deepcopy
from lib.grafo import Grafo
from colorama import Fore, init as color

color()

grafo = Grafo.retorna_grafo("caminho_fulaninho")

origem = "v1"
destinos = ["v3", "v4", "v19", "v26", "v28"]

print(
    f"{Fore.YELLOW} A proposta é utilizar o algoritmo de djikstra para "
    f"encontrar o menor caminho que fulaninho deve percorrer para visitar "
    f"todas as lojas de eletrônicos.{Fore.RESET}\n")
print(
    f"{Fore.YELLOW} Para isso, o algoritmo foi aplicado a partir da casa de "
    f"fulaninho e, cada vez que uma loja era alcançada, o algoritmo "
    f"repetia-se partindo de lá.{Fore.RESET}\n")
input()


# noinspection PyUnboundLocalVariable
def dijkstra(grafo, vertice_origem, vertices_destino):
    """
    Implementação do algoritmo de dijkstra. Recebe o vértice de
    origem e retorna listas de distância e 'path' para todos os
    vértices do grafo.
    Método adaptado para parar assim que o primeiro dos vértices destino
     entrar em S.
    """
    dist = [float('inf') for i in range(len(grafo._vertices))]
    path = ['-' for i in range(len(grafo._vertices))]
    s = [vertice_origem]
    not_s = deepcopy(grafo._vertices)
    not_s.remove(vertice_origem)
    dist[grafo._vertices.index(origem)] = 0

    v_atual = vertice_origem

    while not_s:
        _adj, _p = grafo._get_adjacentes_e_pesos(v_atual)
        adjacentes, pesos = [], []
        for idx, vertice in enumerate(_adj):
            if vertice in not_s:
                adjacentes.append(_adj[idx])
                pesos.append(_p[idx])

        for idx, vertice in enumerate(adjacentes):
            if dist[grafo._vertices.index(vertice)] > \
                    dist[grafo._vertices.index(v_atual)] + pesos[idx]:
                dist[grafo._vertices.index(vertice)] = \
                    dist[grafo._vertices.index(v_atual)] + pesos[idx]
                path[grafo._vertices.index(vertice)] = v_atual

        min_dist = float('inf')
        for vertice in not_s:
            if dist[grafo._vertices.index(vertice)] < min_dist:
                min_dist = dist[grafo._vertices.index(vertice)]
                v_atual = vertice

        s.append(v_atual)
        not_s.remove(v_atual)
        if v_atual in vertices_destino:
            break

    return dist, path, v_atual


def get_menor_caminho(grafo, vertice_origem, vertice_destino, path_lista):
    """
    Utiliza o retorno do método djikstra para retornar o menor
    caminho completo entre dois vértices. Devem ser informados
    vértice de origem e vértice de destino.
    """
    caminho = [vertice_destino]
    v = vertice_destino
    while v != vertice_origem:
        v = path_lista[grafo._vertices.index(v)]
        caminho.append(v)
    caminho = caminho[::-1]
    return caminho


def _caminho_format(lista_caminho):
    """
    Método que formata o caminho para melhor leitura.
    """
    c_form = f"{Fore.YELLOW}{lista_caminho[0]}{Fore.RESET} > "
    for vertice in lista_caminho[1:-1:]:
        c_form += f"{vertice} > "
    c_form += f"{Fore.YELLOW}{lista_caminho[-1]}{Fore.RESET}"
    return c_form


caminho_completo = ["v1"]
distancia_acumulada = 0
while destinos:
    dist, path, mais_proximo = dijkstra(grafo, origem, destinos)
    caminho = get_menor_caminho(grafo, origem, mais_proximo, path)
    caminho_completo += caminho[1::]
    distancia_percorrida = dist[grafo._vertices.index(mais_proximo)]
    distancia_acumulada += distancia_percorrida
    print(f"{Fore.YELLOW}Ponto de Partida: {origem}{Fore.RESET}")
    print(f"\nFármacia mais proxima: {Fore.YELLOW}{mais_proximo}{Fore.RESET}")
    print(
        f"Caminho entre {origem} e {mais_proximo}: "
        f"{_caminho_format(caminho)}"
        f"\nDistancia percorrida: {distancia_percorrida}"
        f"\nDistancia acumulada: {distancia_acumulada}")

    destinos.remove(mais_proximo)
    origem = mais_proximo
    print(f"\nDestinos Restantes: {destinos}")
    input()

print(
    f"\n{Fore.YELLOW}Como não existem mais destinos, o algoritmo acaba "
    f"aqui.{Fore.RESET}")
print(f"Caminho completo de fulaninho: {_caminho_format(caminho_completo)}")
print(f"Distância total percorrida: {distancia_acumulada}")

print(f"{Fore.YELLOW}\nENTER para finalizar{Fore.RESET}")
input()
