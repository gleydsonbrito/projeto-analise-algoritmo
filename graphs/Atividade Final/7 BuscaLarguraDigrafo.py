import collections

digrafo = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2], 4: [3, 1], 5: [4, 1]}


def buscaEmLarguraDigrafo(D, s):
    resultado = []
    print('Coloca o {} na fila'.format(s))
    visitado, F = set(), collections.deque([s])
    visitado.add(s)

    while len(F) > 0:
        arco = F.popleft()
        print('desenfileirou o vertice {}'.format(arco))
        resultado.append(arco)

        # se não foi visitado
        # visita e enfileira
        for v in D[arco]:
            if v not in visitado:
                print('Visitando o vertice {}'.format(v))
                visitado.add(v)
                print('Enfileirou {}'.format(v))
                F.append(v)
    return resultado


print('Resultado: ', buscaEmLarguraDigrafo(digrafo, 3))
