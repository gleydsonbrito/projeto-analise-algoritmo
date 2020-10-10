import collections

grafo = {15: [13, 17, 19], 18: [15], 12: [13], 20: [16, 19], 19: [
    15, 20, 14], 13: [12, 15, 14], 16: [13, 15, 20], 14: [13, 19, 17], 17: [14, 15, 19]}


def BuscaEmLarguraDistancia(G, s):
    p = 0
    resultado = []
    distvu = 0
    print('Coloca o {} na fila'.format(s))
    visitado, F = set(), collections.deque([s])
    visitado.add(s)

    while len(F) > 0:
        p += 1
        vertice = F.popleft()
        print('Desenfileirou o vértice {}'.format(vertice))
        resultado.append(vertice)

        # se não foi visitado
        # visita e enfileira
        for v in G[vertice]:
            p += 1
            if v not in visitado:
                print('Visitando o vértice {}'.format(v))
                visitado.add(v)
                print('Incrementa a distancia')
                distvu = distvu + 1
                print('Enfileirou {}'.format(v))
                F.append(v)
    v = resultado[0]
    u = resultado[len(resultado)-1]
    print('Passos: {}'.format(p))
    print('Distancia {} até {} = {}'.format(v, u, distvu))

    return resultado


print('Resultado: ', BuscaEmLarguraDistancia(grafo, 20))
