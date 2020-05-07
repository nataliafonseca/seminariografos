from lib.grafo import Grafo
from lib.arvore import Arvore
from colorama import Fore, init as color

color()

grafo = Grafo.retorna_grafo("heroi_e_moedas")

print(
    f"{Fore.YELLOW} A proposta é utilizar busca em profundidade para "
    f"auxiliar o herói a coletar todas as moedas. O algoritmo foi aplicado "
    f"até que a pilha fosse zerada ou todas as moedas obtidas.{Fore.RESET}\n")

vertice_origem = "1"
moedas = ["5", "9", "12", "15", "16", "18", "21", "25", "28"]

print(
    f"Vértice Origem: {vertice_origem}"
    f"\nVértices Destino: {moedas}\n")

pilha = [vertice_origem]
vertices_visitados = Arvore(vertice_origem)

print(
    f"{Fore.YELLOW}Para dar inicio ao algoritmo, adicionamos o vértice de "
    f"origem à pilha e à Árvore de vértices visitados. Temos: {Fore.RESET}")
print(f"PILHA: {pilha}")
print(f"MOEDAS RESTANTES: {moedas}")
print(f"VÉTICES VISITADOS:")
vertices_visitados.imprimir()
input()

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
        print()
    print(
        f"\n{Fore.YELLOW}Se houver vértices adjacentes ao ultimo da Pilha, "
        f"um deles é adicionados à Pilha e se torna o novo vértice a ser "
        f"trabalhado. Caso não hajá, o ultimo elemento é retirado da pilha e "
        f"voltamos a explorar ao elemento anterior. Temos: {Fore.RESET}")
    print(f"PILHA: {pilha}")
    print(f"MOEDAS RESTANTES: {moedas}")
    print(f"VÉTICES VISITADOS:")
    vertices_visitados.imprimir()
    input()

print(
    f"{Fore.YELLOW}Finalmente o nosso herói conseguiu resgatar todas as "
    f"moedas. Assim, finalizou o algoritmo. Podemos notar que, "
    f"para recuperar as moedas todos os vértices precisaram ser visitado. "
    f"Assim, se o algoritmo continuasse, iria apenas ocorrer o "
    f"desempilhamento dos vértices restantes na pilha. "
    f"{Fore.RESET}")
input()

print(f"{Fore.YELLOW}\nENTER para finalizar{Fore.RESET}")
input()
