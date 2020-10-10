from collections import defaultdict
inf = float('Inf')

# retorna o vertice com a menor distância de sua origem


def menor_distancia(dist, visitados):

    (minimo, mVertice) = (inf, 0)
    for vertice in range(len(dist)):
        if minimo > dist[vertice] and visitados[vertice] == False:
            (minimo, mVertice) = (dist[vertice], vertice)

    return mVertice


# Dijkstra para o grafo modificado
def Dijkstra(G, novo_grafo, origem, p):

    # número de vertices do grafo
    numer_vertices = len(G)

    # Checa se o vertice está na arvore de caminho mínimo
    esta_na_arvore_caminho_minimo = defaultdict(lambda: False)

    # Menor distância de todos os vertices a partir de sua fonte
    dist = [inf] * numer_vertices

    dist[origem] = 0

    for vertice in range(numer_vertices):
        p += 1
        # O vertice atual que está na menos distancia
        # de sua fonte ainda não foi incluido na
        # arvore de menor caminho
        atual = menor_distancia(dist, esta_na_arvore_caminho_minimo)
        esta_na_arvore_caminho_minimo[atual] = True

        for vertice in range(numer_vertices):
            p += 1
            if ((esta_na_arvore_caminho_minimo[vertice] == False) and
                (dist[vertice] > (dist[atual] +
                                  novo_grafo[atual][vertice])) and
                    (G[atual][vertice] != 0)):

                dist[vertice] = (dist[atual] +
                                 novo_grafo[atual][vertice])
        print('Passos: {}'.format(p))
    # Imprime a menor distância de cada vertice desde sua origem
    for vertice in range(numer_vertices):
        if dist[vertice] == float('inf'):
            dist[vertice] = 'Não há caminho'
        print('vertice ' + str(vertice) + ' é ' + str(dist[vertice]))

# Calcula a menor distancia de cada fonte para
# para outro vertice usando Bellman-Ford


def BellmanFord(arestas, G, numero_vertices, p):

    # Adiciona o origem s e calcula o vertice mais próximo
    # de cada outro vertice
    dist = [inf] * (numero_vertices + 1)
    dist[numero_vertices] = 0

    for i in range(numero_vertices):
        p += 1
        arestas.append([numero_vertices, i, 0])

    for i in range(numero_vertices):
        p += 1
        for (origem, destino, peso) in arestas:
            p += 1
            if((dist[origem] != inf) and
                    (dist[origem] + peso < dist[destino])):
                dist[destino] = dist[origem] + peso
    print('Passos: {}'.format(p))
    return dist[0:numero_vertices]

# Implementa Algoritmo de Johnson


def johnson_algoritmo(G, p):

    arestas = []

    # cria a lista de arestas com o Bellman-Ford
    for i in range(len(G)):
        p += 1
        for j in range(len(G[i])):
            p += 1
            if G[i][j] != 0:
                arestas.append([i, j, G[i][j]])
    print('Passos: {}'.format(p))
    # o pesos são usados para modificar os pesos originais
    pesos_modificados = BellmanFord(arestas, G, len(G), p)

    grafo_modificado = [[0 for x in range(len(G))] for y in
                        range(len(G))]

    # Modifica os pesos para eliminar os pesos negativos
    for i in range(len(G)):
        p += 1
        for j in range(len(G[i])):
            p += 1
            if G[i][j] != 0:
                grafo_modificado[i][j] = (G[i][j] +
                                          pesos_modificados[i] - pesos_modificados[j])
    print('Passos: {}'.format(p))
    print('Grafo modificado: ' + str(grafo_modificado))

    # Executa o dijkstra para cada vertice fonte
    for origem in range(len(G)):
        print('\nMenor distancia do vertice ' +
              str(origem) + ' para o\n')
        Dijkstra(G, grafo_modificado, origem, p)


grafo = [[0, -5, 2, 3],
         [0, 0, 4, 0],
         [0, 0, 0, 1],
         [0, 0, 0, 0]]

johnson_algoritmo(grafo, 0)
