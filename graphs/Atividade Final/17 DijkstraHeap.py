from collections import defaultdict
from heapq import *


def dijkstra(arcos, f, t, D=None):
    D = defaultdict(list)
    for l, r, c in arcos:
        D[l].append((c, r))

    q, visitados, minimo = [(0, f, ())], set(), {f: 0}
    while q:
        (w, v, caminho) = heappop(q)
        if v not in visitados:
            visitados.add(v)
            caminho = (v, caminho)
            if v == t:
                return (w, caminho)

            for c, v2 in D.get(v, ()):
                if v2 in visitados:
                    continue
                anterior = minimo.get(v2, None)
                prox = w + c
                if anterior is None or prox < anterior:
                    minimo[v2] = prox
                    heappush(q, (prox, v2, caminho))

    return float("inf")


if __name__ == "__main__":
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

    print('Caminho mínimo de F a G', dijkstra(edges, "F", "G"))
