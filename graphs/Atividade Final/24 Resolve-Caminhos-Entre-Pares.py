INF = float('inf')


def FloydMarshallTpoDowb():
    return [[1, 3, INF, 5],
            [2, 2, INF, 4],
            [INF, 0, 3, INF],
            [INF, INF, 4, 1]]


def Resolve_Caminhos_Entre_Pares(D=None, w=None):
    W = FloydMarshallTpoDowb()
    for i in range(4):
        if W[i][i] < 0:
            return NotImplemented
    return print(W, end='\n')


print(Resolve_Caminhos_Entre_Pares())
