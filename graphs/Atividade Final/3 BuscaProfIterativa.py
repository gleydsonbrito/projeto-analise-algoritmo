G = {'A': set(['B', 'C']),
     'B': set(['A', 'D', 'E']),
     'C': set(['A', 'F']),
     'D': set(['B']),
     'E': set(['B', 'F']),
     'F': set(['C', 'E'])}


def BuscaProfIterativa(G, s):
    print('Inicia pelo vertice {}'.format(s))
    visitado = set()
    print('Empilha {}'.format(s))
    P = [s]
    while len(P) > 0:
        vertice = P.pop()
        print('Desempilha {}'.format(vertice))
        if vertice not in visitado:
            visitado.add(vertice)
            print('Visita o vétice {}'.format(vertice))
            P.extend(G[vertice] - visitado)
            print('Tira {} do grafo G'.format(vertice))
    return visitado


print('Resultado: ', BuscaProfIterativa(G, 'A'))
