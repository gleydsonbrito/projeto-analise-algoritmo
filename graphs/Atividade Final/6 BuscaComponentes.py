grafo = {
    0: {0, 1, 3},
    1: {1, 3, 5},
    2: set(),
    3: {3, 4, 5},
    4: {6},
    5: {3, 4, 5, 7},
    6: set(),
    7: {3, 6},
    8: set(),
    9: {4, 8}}


def quantidadeComponentes(componentes):
    return print('Quantidade de componentes: ', len(componentes))


def grupos(G):
    visitado = set()
    resultado = []
    for v in G:
        if v not in visitado:
            conectados, visitado = gruposConectados(
                v, visitado)
            resultado.append(conectados)
    return resultado


def gruposConectados(v, visitado):
    resultado = []
    vertices = set([v])
    while vertices:
        v = vertices.pop()
        visitado.add(v)
        vertices = vertices or grafo[v] - visitado
        resultado.append(v)
    return resultado, visitado


quantidadeComponentes(grupos(grafo))
