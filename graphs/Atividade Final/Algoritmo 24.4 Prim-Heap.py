from collections import defaultdict
import heapq


grafo = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1, 'G': 1},
    'G': {'F': 1},
}


def criarArvoreGeradora(G, s):
    print('Vertice de entrada {}'.format(s))
    arvoreGeradoraMinima = defaultdict(set)
    visitados = set([s])
    print('Visita {}'.format(s))
    arestas = [
        (d, s, v)
        for v, d in G[s].items()
    ]
    heapq.heapify(arestas)

    while arestas:
        d, u, v = heapq.heappop(arestas)
        print('Vai para o vizinho mais proximo: {}'.format(v))
        if v not in visitados:
            visitados.add(v)
            print('Visitando {}'.format(v))
            arvoreGeradoraMinima[u].add(v)
            print('Liga {} com {}'.format(u, v))
            for proximo, d in G[v].items():
                if proximo not in visitados:
                    print('Verifica distancia para {}'.format(proximo))
                    heapq.heappush(arestas, (d, v, proximo))

    return arvoreGeradoraMinima


print('Arvore geradora minima: ', criarArvoreGeradora(grafo, 'C'))
