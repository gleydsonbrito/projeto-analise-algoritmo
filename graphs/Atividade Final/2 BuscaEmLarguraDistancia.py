import collections

graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2], 4: [3, 1], 5: [4, 1]}


def BuscaEmLarguraDistancia(G, s):
    resultado = []
    distvu = 0
    print('Coloca o {} na fila'.format(s))
    visitado, F = set(), collections.deque([s])
    visitado.add(s)

    while len(F) > 0:
        vertice = F.popleft()
        print('Desenfileirou o vértice {}'.format(vertice))
        resultado.append(vertice)

        # se não foi visitado
        # visita e enfileira
        for v in G[vertice]:
            if v not in visitado:
                print('Visitando o vértice {}'.format(v))
                visitado.add(v)
                print('Incrementa a distancia')
                distvu = distvu + 1
                print('Enfileirou {}'.format(v))
                F.append(v)
    v = resultado[0]
    u = resultado[len(resultado)-1]
    print('Distancia {} até {} = {}'.format(v, u, distvu))

    return resultado


print('Resultado: ', BuscaEmLarguraDistancia(graph, 4))
