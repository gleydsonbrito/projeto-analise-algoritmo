grafo = {
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


def quantidadeComponentes(componentes):
    return print('Total de componentes conexos: ', len(componentes))


def grupos(G, p):
    visitado = set()
    resultado = []
    for v in G:
        p += 1
        if v not in visitado:
            print('{} ainda não foi visitado'.format(v))
            conectados, visitado = gruposConectados(
                v, visitado, p)

            print('O componente {} está no componente {}'.format(
                v, conectados))
            resultado.append(conectados)
    print('Passos: {}'.format(p))
    return resultado


def gruposConectados(v, visitado, p):
    resultado = []
    vertices = set([v])
    print('Visitando {} e verificando suas conexões'.format(v))
    while vertices:
        p += 1
        v = vertices.pop()

        visitado.add(v)
        vertices = vertices or grafo[v] - visitado

        resultado.append(v)
    print('Passos: {}'.format(p))
    return resultado, visitado


quantidadeComponentes(grupos(grafo, 0))
