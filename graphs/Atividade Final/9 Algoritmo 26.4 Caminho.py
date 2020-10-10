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
# função que encontra o caminho entre dois vertices


def encontra_caminho(D, v_inicial, v_final, p, caminhos=[]):
    p += 1
    print('Encontrar o caminho de {} a {}'.format(v_inicial, v_final))
    # adiciona o vertice inicial como primeiro elemento do caminho
    caminhos = caminhos + [v_inicial]
    # checa se o vertice final e inicial são o mesmo
    if v_inicial == v_final:
        return caminhos

    # checa se o vertice inicial pertence ao conjunto v(D)
    if v_inicial not in D:
        return 'Vertice inválido'

    # percorre todos os vertices para identificar se há caminho entre eles
    for v in D[v_inicial]:
        p += 1
        if v not in caminhos:
            # se há caminho faz uma chamada recursiva a partir desse vértice
            newpath = encontra_caminho(D, v, v_final, p, caminhos)
            if newpath:
                return newpath
        print('Passos: {}'.format(p))
    return 'Não há caminho'


print('Caminho: ', encontra_caminho(grafo, 1, 9, 0))
