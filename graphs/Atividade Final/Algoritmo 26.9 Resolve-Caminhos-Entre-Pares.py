INF = 1000000000


def floyd_warshall(vertice, M_adjacencias):
    # calcula o menor camimho entre todos os pares
    for k in range(0, vertice):
        for i in range(0, vertice):
            for j in range(0, vertice):
                # relax the distance from i to j by allowing vertex k as intermediate vertex
                #
                # consider which one is better, going through vertex k or the previous value
                M_adjacencias[i][j] = min(
                    M_adjacencias[i][j], M_adjacencias[i][k] + M_adjacencias[k][j])

    print('Montando a matriz de resultado')
    print('lin/col significa vertice de origem (lin) e (col) vertice de destino')
    print('A relação A[i][j] representa a distância')
    print("lin/col", end='')
    for i in range(0, vertice):
        print("\t{:d}".format(i+1), end='')
    print()
    for i in range(0, vertice):
        print("{:d}".format(i+1), end='')
        for j in range(0, vertice):
            print("\t{:d}".format(M_adjacencias[i][j]), end='')
        print()


ma = [
    [0,   1, 3, INF],
    [1,   0, 1, INF],
    [3,   1, 0,   2],
    [INF, INF, 2,   0]
]
floyd_warshall(4, ma)
