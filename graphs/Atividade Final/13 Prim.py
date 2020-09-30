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
    # guarda os vertices selecionados
    selecionados = [0]*len(G)
    selecionados[0] = True
    while (w < numeroVertices - 1):
        minimo = 9999999
        x = 0
        y = 0
        for i in range(numeroVertices):
            if selecionados[i]:
                for j in range(numeroVertices):
                    if ((not selecionados[j]) and G[i][j]):
                        if minimo > G[i][j]:
                            minimo = G[i][j]
                            x = i
                            y = j
        arvoreGeradoraMinima.append(str(G[x][y]))
        a.append([x, y])
        selecionados[y] = True
        w = w + 1


Prim(G, w)
print('Arvore geradora mínima: ', arvoreGeradoraMinima)
print('Arestas: ', a)
