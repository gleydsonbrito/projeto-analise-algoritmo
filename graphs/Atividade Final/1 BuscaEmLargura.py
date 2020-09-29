import collections

graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2], 4: [3, 1], 5: [4, 1]}


def buscaEmLargura(G, s):
    resultado = []
    print('Coloca o {} na fila'.format(s))
    visitado, F = set(), collections.deque([s])
    visitado.add(s)

    while len(F) > 0:
        vertice = F.popleft()
        print('desenfileirou o vértice {}'.format(vertice))
        resultado.append(vertice)

        # se não foi visitado
        # visita e enfileira
        for v in G[vertice]:
            if v not in visitado:
                print('Visitando o vértice {}'.format(v))
                visitado.add(v)
                print('Enfileirou {}'.format(v))
                F.append(v)
    return resultado


print('Resultado: ', buscaEmLargura(graph, 4))
