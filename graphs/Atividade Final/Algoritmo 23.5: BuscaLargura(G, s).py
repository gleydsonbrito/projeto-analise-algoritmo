import collections

grafo = {15: [13, 17, 19], 18: [15], 12: [13], 20: [16, 19], 19: [
    15, 20, 14], 13: [12, 15, 14], 16: [13, 15, 20], 14: [13, 19, 17], 17: [14, 15, 19]}


def buscaEmLargura(G, s):
    p = 0
    i = 0
    resultado = []
    print('Coloca o {} na lista'.format(s))
    visitado, F = set(), collections.deque([s])
    visitado.add(s)

    while len(F) > 0:
        p = p + 1
        vertice = F.popleft()
        resultado.append(vertice)
        print(resultado)
        print('Verifica se há vizinhos de {} para visitar'.format(
            resultado[i]))

        # se não foi visitado
        # visita e enfileira
        for v in G[vertice]:
            p = p + 1
            if v not in visitado:
                print('Visitando {}'.format(v))
                visitado.add(v)
                F.append(v)
        i += 1
    print('Número de passos: {}'.format(p))
    return resultado


print('Saída : {}'.format(buscaEmLargura(grafo, 20)))
