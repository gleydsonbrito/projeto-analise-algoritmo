digrafo = {'A': set(['B', 'C']),
           'B': set(['A', 'D', 'E']),
           'C': set(['A', 'F']),
           'D': set(['B']),
           'E': set(['B', 'F']),
           'F': set(['C', 'E'])}


def BuscaProfDigrafo(D, s):
    print('Inicia pelo vertice {}'.format(s))
    visitado = set()
    print('Empilha {}'.format(s))
    P = [s]
    while len(P) > 0:
        arco = P.pop()
        print('Desempilha {}'.format(arco))
        if arco not in visitado:
            visitado.add(arco)
            print('Visita o vétice {}'.format(arco))
            P.extend(D[arco] - visitado)
            print('Tira {} do digrafo'.format(arco))
    return visitado


print('Resultado: ', BuscaProfDigrafo(digrafo, 'A'))
