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


def BuscaProfDigrafo(D, s):
    print('Inicia pelo vertice {}'.format(s))
    visitado = set()
    print('Empilha {}'.format(s))
    P = [s]
    while len(P) > 0:
        arco = P.pop()
        print('Desempilha {}'.format(arco))
        print('Visita os {} vizinhos de {}'.format(D[arco], arco))
        if arco not in visitado:
            visitado.add(arco)
            print('Visita o vétice {}'.format(arco))
            P.extend(D[arco] - visitado)
            print('Tira {} do digrafo'.format(arco))
        print('Pilha para ser visitada {}'.format(P))
    return visitado


print('Resultado: ', BuscaProfDigrafo(digrafo, 13))
