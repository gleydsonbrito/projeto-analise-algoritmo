# Funçao recursiva que imprime o caminho de um vertice u a partir de um vertice v
def imprimir_caminho(caminho, v, u):

    if caminho[v][u] == v:
        return

    imprimir_caminho(caminho, v, caminho[v][u])
    print(caminho[v][u], end=' ')


# Função que imprime o menor caminho
def imprime_resultado(path, N):

    for v in range(N):
        for u in range(N):
            if u != v and path[v][u] != -1:
                print(f"O menor caminmho de {v} até-> {u} é ({v}", end=' ')
                imprimir_caminho(path, v, u)
                print(f"{u})")


# Função que executa o algoritmo Floyd-Warshall
def floydWarshall(matriz_adjacencia, N):
    custo = matriz_adjacencia.copy()
    caminho = [[None for x in range(N)] for y in range(N)]

    # inicializando os custos
    for v in range(N):
        for u in range(N):
            if v == u:
                caminho[v][u] = 0
            elif custo[v][u] != float('inf'):
                caminho[v][u] = v
            else:
                caminho[v][u] = -1

    # execução do algoritmo
    for k in range(N):
        for v in range(N):
            for u in range(N):
                # se o vertice  k está no menor caminho entre u v,
                # então atualiza o valor do custo [u,v], do caminho [u][v]

                if custo[v][k] != float('inf') and custo[k][u] != float('inf') \
                        and (custo[v][k] + custo[k][u] < custo[v][u]):
                    custo[v][u] = custo[v][k] + custo[k][u]
                    caminho[v][u] = caminho[k][u]

            # se o elemento diagonal é negativo, o
            # grafo contém um ciclo de pesos negativos

            if custo[v][v] < 0:
                print("Uma aresta negativa foi encontrada")
                return
    # imprime o menor caminho entre todos os pares de vertices
    imprime_resultado(caminho, N)


N = 4
M = float('inf')

# representação da matriz de adjacência
mat_adja = [
    [0, M, -2, M],
    [4, 0, 3, M],
    [M, M, 0, 2],
    [M, -1, M, 0]
]

floydWarshall(mat_adja, N)
