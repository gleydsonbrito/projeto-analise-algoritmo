from collections import defaultdict
from heapq import *

# Dijkstra usando heap


def dijkstra(arcos, s, t, D=None):
    D = defaultdict(list)
    for l, r, c in arcos:
        D[l].append((c, r))

    heap, visitados, minimo = [(0, s, ())], set(), {s: 0}

    while heap:
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
                if v2 in visitados:
                    continue
                predecessor = minimo.get(v2, None)

                prox = w + c
                print('Distancia total para {} = {}'.format(v2, prox))
                if predecessor is None or prox < predecessor:
                    minimo[v2] = prox
                    print('Mais proximo?', prox)
                    heappush(heap, (prox, v2, caminho))

    return float("inf")


edges = [
    ("A", "B", 7),
    ("A", "D", 5),
    ("B", "C", 8),
    ("B", "D", 9),
    ("B", "E", 7),
    ("C", "E", 5),
    ("D", "E", 15),
    ("D", "F", 6),
    ("E", "F", 8),
    ("E", "G", 9),
    ("F", "G", 11)
]

print("=== Dijkstra ===\n\n")

print('Caminho mínimo de A a E', dijkstra(edges, "A", "E"))
