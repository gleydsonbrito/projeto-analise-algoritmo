import collections

digrafo = {
    1: {2, 3},
    2: {1, 3, 4, 8, 11},
    3: {1, 2, 4, 5},
    4: {2, 3, 8, 7, 9},
    5: {3, 6},
    6: {5},
    7: {4, 10, 11},
    8: {2, 4},
    9: {4, 11},
    10: {4, 11},
    11: {7, 9, 10},
    12: {13},
    13: {14, 15, 16},
    14: {13, 17, 19},
    15: {13, 17, 18, 19},
    16: {13, 15, 20},
    17: {14, 15, 19},
    18: {15},
    19: {14, 15, 17, 20},
    20: {16, 19}}


def buscaEmLarguraDigrafo(D, s):
    resultado = []
    print('Coloca o {} na fila'.format(s))
    visitado, F = set(), collections.deque([s])
    visitado.add(s)
    print('Visita {}'.format(s))

    while len(F) > 0:
        arco = F.popleft()

        print('desenfileirou o vertice {}'.format(arco))
        resultado.append(arco)
        print('Visitas os vizinhos {} de {}'.format(D[arco], arco))

        # se não foi visitado
        # visita e enfileira
        for v in D[arco]:
            if v not in visitado:
                print('Visitando o vertice {}'.format(v))
                visitado.add(v)
                print('Enfileirou {}'.format(v))
                F.append(v)
        print('Fila para ser visitada {}'.format(F))
    return resultado


print('Resultado: ', buscaEmLarguraDigrafo(digrafo, 13))
