from collections import defaultdict
from heapq import *

# Dijkstra usando heap


def dijkstra(arcos, s, t, D=None):
    p = 0
    D = defaultdict(list)
    for l, r, c in arcos:
        D[l].append((c, r))

    heap, visitados, minimo = [(0, s, ())], set(), {s: 0}

    while heap:
        p += 1
        (w, v, caminho) = heappop(heap)
        print('Custo caminho total', w)
        print('Vertice atual ', v)
        print('Caminmho: ', caminho)
        if v not in visitados:
            visitados.add(v)
            print('Visitando {}'.format(v))
            caminho = (v, caminho)
            if v == t:
                return (w, caminho)

            for c, v2 in D.get(v, ()):
                p += 1
                if v2 in visitados:
                    continue
                predecessor = minimo.get(v2, None)

                prox = w + c
                print('Distancia total para {} = {}'.format(v2, prox))
                if predecessor is None or prox < predecessor:
                    minimo[v2] = prox
                    print('Mais proximo?', prox)
                    heappush(heap, (prox, v2, caminho))
        print('Passos: {}'.format(p))
    return float("inf")


edges = [
    ("2", "1", 8),
    ("2", "7", 3),
    ("3", "5", 8),
    ("4", "1", 1),
    ("4", "8", 2),
    ("5", "1", 9),
    ("5", "4", 5),
    ("5", "6", 1),
    ("6", "3", 2),
    ("6", "8", 3),
    ("6", "9", 7),
    ("7", "5", 1),
    ("7", "3", 0),
    ("8", "5", 1),
    ("8", "9", 3)
]

print("=== Dijkstra ===\n\n")

print('O peso e o caminho mínimo de 2 a 7: ', dijkstra(edges, "2", "9"))
