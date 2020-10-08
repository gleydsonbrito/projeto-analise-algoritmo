import collections

grafo = {15: [13, 17, 19], 18: [15], 12: [13], 20: [16, 19], 19: [
    15, 20, 14], 13: [12, 15, 14], 16: [13, 15, 20], 14: [13, 19, 17], 17: [14, 15, 19]}


def buscaEmLargura(G, s):
    resultado = []
    print('Coloca o {} na fila'.format(s))
    visitado, F = set(), collections.deque([s])
    visitado.add(s)

    while len(F) > 0:
        vertice = F.popleft()
        #print('desenfileirou o vértice {}'.format(vertice))
        resultado.append(vertice)
        print(resultado)

        # se não foi visitado
        # visita e enfileira
        for v in G[vertice]:
            if v not in visitado:
                print('Visitando o vértice {}'.format(v))
                visitado.add(v)
                #print('Enfileirou {}'.format(v))
                F.append(v)
    return resultado


print('Saída : ', buscaEmLargura(grafo, 20))
