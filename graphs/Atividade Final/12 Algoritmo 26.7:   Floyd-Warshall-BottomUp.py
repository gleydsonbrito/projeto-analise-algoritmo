nivel = 4

INF = float('inf')

# implementação do algoritmo


def floyd_warshall(G):
    p = 0
    distance = list(map(lambda i: list(map(lambda j: j, i)), G))

    # adicionando vertices individualmente
    for k in range(nivel):
        p += 1
        for i in range(nivel):
            p += 1
            for j in range(nivel):
                p += 1
                print('Estamos no G[{}][{}]'.format(i, j))
                distance[i][j] = min(
                    distance[i][j], distance[i][k] + distance[k][j])
                print('Pega o mais proximo entre G[{}][{}] = {} e a soma entre G[{}][{}]={} e G[{}][{}] = {} soma = {}'.format(
                    i, j, distance[i][j], i, k, distance[i][k], k, j, distance[k][j], distance[i][k]+distance[k][j]))
                print('Pega {}'.format(distance[i][j]))
    imprimir(distance)
    print('Passos: {}'.format(p))


def imprimir(distance):
    for i in range(nivel):
        for j in range(nivel):
            if(distance[i][j] == INF):
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")
        print(" ")


G = [[1, 3, INF, 5],
     [2, 2, INF, 4],
     [INF, 0, 3, INF],
     [INF, INF, 4, 1]]

floyd_warshall(G)
print('a matriz resultado demonstra a distancia minima entre os elementos i, j da matriz')
