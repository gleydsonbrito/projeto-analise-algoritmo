nivel = 4

INF = float('inf')

# implementação do algoritmo


def floyd_warshall(G):
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # adicionando vertices individualmente
    for k in range(nivel):
        for i in range(nivel):
            for j in range(nivel):
                distance[i][j] = min(
                    distance[i][j], distance[i][k] + distance[k][j])
                print('Pega o menor entre {} e {}'.format(
                    distance[i][j], distance[i][k] + distance[k][j]))
                print('Pega {}'.format(distance[i][j]))
    imprimir(distance)


def imprimir(distance):
    for i in range(nivel):
        for j in range(nivel):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


# a matriz resultado demonstra a distancia minima entre os elementos i, j da matriz
G = [[1, 3, INF, 5],
     [2, 2, INF, 4],
     [INF, 0, 3, INF],
     [INF, INF, 4, 1]]

floyd_warshall(G)
