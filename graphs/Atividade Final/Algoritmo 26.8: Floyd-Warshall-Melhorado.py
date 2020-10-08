inf = float('inf')

# Matriz de Adjacência
M = [
    [0,     2,   5,   inf,   inf,   inf,   inf,   inf,  inf,   inf,   inf],
    [2,     0,   8,     1,   inf,   inf,   inf,     9,  inf,   inf,     8],
    [5,   inf,   0,     5,     3,   inf,   inf,   inf,  inf,   inf,   inf],
    [inf,   1,   5,     0,   inf,   inf,     4,     2,    6,   inf,   inf],
    [inf, inf,   5,   inf,     0,     3,   inf,   inf,  inf,   inf,   inf],
    [inf, inf, inf,   inf,     3,     0,   inf,   inf,    4,   inf,   inf],
    [inf, inf, inf,     4,   inf,   inf,     0,   inf,  inf,     3,     1],
    [inf,   9, inf,     2,   inf,   inf,   inf,     0,  inf,   inf,   inf],
    [inf, inf, inf,     6,   inf,     4,   inf,   inf,    0,   inf,     9],
    [inf, inf, inf,   inf,   inf,   inf,     3,   inf,  inf,     0,     2],
    [inf, inf, inf,   inf,   inf,   inf,     1,   inf,    9,     2,     0], ]


def floyd_warshall(Md):
    exe = 0
    v = len(Md)
    Md = Md
    for k in range(v):
        exe += 1
        prox_md = Md
        for i in range(v):
            exe += 1
            for j in range(v):
                exe += 1
                print('Consulta o elemento {}'.format(Md[i][j]))
                print('Substitui {} pelo menor valor entre {} e {}'.format(
                    Md[i][j], Md[i][j], Md[i][k]+Md[k][j]))
                prox_md[i][j] = min(Md[i][j],
                                    Md[i][k] + Md[k][j])
                print('Matriz na posição M[i][j] = {}'.format(Md[i][j]))
        Md = prox_md
    print('Retorna o resultado apos {} execuções'.format(exe))
    return Md


print(floyd_warshall(M))
