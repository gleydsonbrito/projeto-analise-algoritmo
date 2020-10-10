grafo = {12: set([13]),
         13: set([12, 14, 15, 16]),
         14: set([13, 17, 19]),
         15: set([13, 16, 17, 18]),
         16: set([13, 15, 20]),
         17: set([15, 19]),
         18: set([15]),
         19: set([14, 15, 17, 20]),
         20: set([16, 19]),
         }

# como é uma função recursiva, colocar os prints
# atrapalha a legibilidade do resultado final
# adicionei os comentários


def buscaProfRecursiva(G, inicio, p, visitado=None):

    resultado = []
    if visitado is None:
        visitado = set()
    # Marca o primeiro vertice como visitado
    visitado.add(inicio)
    # imprimindo as saídas
    print('V:', inicio, end=' -> ')
    # percorre o próximo vertice que está em G - visitados
    for proximo in G[inicio] - visitado:

        buscaProfRecursiva(G, proximo, p, visitado)

    return visitado


buscaProfRecursiva(grafo, 15, p)
print('Passos: {}'.format(p))
