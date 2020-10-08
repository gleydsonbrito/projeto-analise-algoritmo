grafo = {1: set([2, 3]),
         2: set([3, 4, 11]),
         3: set([2, 4, 5]),
         4: set([2, 3, 7, 8]),
         5: set([3, 6]),
         6: set([5]),
         7: set([4, 10, 11]),
         8: set([2, 4]),
         9: set([4, 11]),
         10: set([7, 11]),
         11: set([7, 9, 10])}


def BuscaProfIterativa(G, s):
    print('Inicia pelo vertice {}'.format(s))
    visitado = set()
    print('Empilha {}'.format(s))
    P = [s]
    while len(P) > 0:
        print('Elementos na pilha {}'.format(P))
        vertice = P.pop()
        print('Desempilha {}'.format(vertice))
        if vertice not in visitado:
            visitado.add(vertice)
            print('Visita o vétice {}'.format(vertice))
            P.extend(G[vertice] - visitado)
            print('Adiciona aos visitados {}'.format(visitado))
            print('Empilha os vizinhos')

    return visitado


print(BuscaProfIterativa(grafo, 3))
