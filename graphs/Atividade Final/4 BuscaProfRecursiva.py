G = {'0': set(['1', '2']),
     '1': set(['0', '3', '4']),
     '2': set(['0']),
     '3': set(['1']),
     '4': set(['2', '3'])}

# como é uma função recursiva, colocar os prints
# atrapalha a legibilidade do resultado final
# adicionei os comentários


def buscaProfRecursiva(G, inicio, visitado=None):
    resultado = []
    if visitado is None:
        visitado = set()
    # Marca o primeiro vertice como visitado
    visitado.add(inicio)
    # imprimindo as saídas
    print('Vertice: ', inicio, end=' -> ')
    # percorre o próximo vertice que está em G - visitados
    for proximo in G[inicio] - visitado:
        buscaProfRecursiva(G, proximo, visitado)
    return visitado


buscaProfRecursiva(G, '2')
