INF = 1000000000


def floyd_warshall(vertice, M_adjacencias):
    p = 0
    # calcula o menor camimho entre todos os pares
    for k in range(0, vertice):
        p += 1
        for i in range(0, vertice):
            p += 1
            for j in range(0, vertice):
                p += 1
                M_adjacencias[i][j] = min(
                    M_adjacencias[i][j], M_adjacencias[i][k] + M_adjacencias[k][j])
    print('Passos: {}'.format(p))
    print('Montando a matriz de resultado')
    print('l/c significa vertice de origem (l=linha) e vertice de destino (c=coluna) ')
    print('A relação A[i][j] representa a distância')
    print("l/c", end='')
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
