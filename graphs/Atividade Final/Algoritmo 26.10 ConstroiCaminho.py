grafo = {1: [2, 3],
         2: [3, 4],
         3: [4, 5, 7],
         4: [3, 1, 4],
         5: [6, 3, 4, 1],
         6: [3, 5, 4]}

# função que encontra o caminho entre dois vertices


def constroi_caminho(grafo, i=None, j=None):
    for i in range(len(grafo)):
        for j in range(len(grafo)):
            print('Encontrar o caminho de {} a {}'.format(i, j))
            print('Caminho: ', encontra_caminho(grafo, i, j))


def encontra_caminho(D, v_inicial, v_final, caminhos=[]):

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
        if v not in caminhos:
            # se há caminho faz uma chamada recursiva a partir desse vértice
            newpath = encontra_caminho(D, v, v_final, caminhos)
            if newpath:
                return newpath
    return 'Não há caminho'


constroi_caminho(grafo)
