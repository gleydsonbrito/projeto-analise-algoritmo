grafo = {12: set([13]),
         13: set([12, 14, 15, 16]),
         14: set([13, 17, 19]),
         15: set([13, 16, 17, 18]),
         16: set([13, 15, 20]),
         17: set([15, 19]),
         18: set([15]),
         19: set([14, 15, 17, 20]),
         20: set([16, 19]),
         }


def buscaProfundidade(G, s):
    C = []
    Pilha = []

    Pilha.append(s)
    print('Empilha {}'.format(s))
    visitados = set()
    print('Visitados {}'.format(visitados))
    visitados.add(s)
    print('Adiciona {} aos visitados'.format(s))

    while (len(Pilha) > 0):
        print('Pilha {}'.format(Pilha))
        vertice = Pilha.pop()
        print('Desempilha {}'.format(vertice))
        v = G[vertice]
        for i in v:
            if i not in visitados:
                Pilha.append(i)
                print('Visitando {}'.format(i))
                visitados.add(i)
        C.append(vertice)
    return C


print('Resulttado : ', buscaProfundidade(grafo, 13))
