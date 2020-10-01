grafo = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D', 'E', 'G'],
         'D': ['C', 'A', 'D'],
         'E': ['F', 'C', 'D', 'A'],
         'F': ['C', 'E', 'D']}

# função que encontra o caminho entre dois vertices


def encontra_caminho(D, v_inicial, v_final, caminhos=[]):
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
        if v not in caminhos:
            # se há caminho faz uma chamada recursiva a partir desse vértice
            newpath = encontra_caminho(D, v, v_final, caminhos)
            if newpath:
                return newpath
    return 'Não há caminho'


print('Caminho: ', encontra_caminho(grafo, 'E', 'D'))
