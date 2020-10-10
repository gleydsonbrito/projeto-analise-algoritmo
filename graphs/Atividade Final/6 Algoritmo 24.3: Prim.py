numeroVertices = 5

# matriz de adjacência
G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

arvoreGeradoraMinima = []
a = []
w = 0


def Prim(G, w):
    p = 0
    # guarda os vertices selecionados
    selecionados = [0]*len(G)
    selecionados[0] = True
    print('Percorrendo os vértices para encontrar o menor peso entre os vertices conectados')
    while (w < numeroVertices - 1):
        p += 1
        minimo = 9999999
        x = 0
        y = 0
        for i in range(numeroVertices):
            p += 1
            #print('Visita {}'.format(i))
            if selecionados[i]:
                #print('{} foi Selecionado? {}'.format(i, selecionados[i]))
                for j in range(numeroVertices):
                    p += 1
                    if G[i][j] != 0:
                        print('Vertice G[{}][{}] tem peso {}'.format(
                            i, j, G[i][j]))
                    else:
                        print(
                            'Entre os vétices G[{}][{}] não há caminho'.format(i, j))
                    if ((not selecionados[j]) and G[i][j]):

                        if minimo > G[i][j]:
                            minimo = G[i][j]
                            print(
                                'Até o momento o vertice mais próximo é {}'.format(minimo))
                            x = i
                            y = j
        print('Passos: {}'.format(p))
        arvoreGeradoraMinima.append(str(G[x][y]))
        print('Adiciona {} à ávore'.format(str(G[x][y])))
        a.append([x, y])
        selecionados[y] = True
        w = w + 1


Prim(G, w)
print('Arvore geradora mínima: ', arvoreGeradoraMinima)
print('Arestas: ', a)
