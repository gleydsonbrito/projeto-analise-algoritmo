pai = dict()
rank = dict()


def makeSet(vertice):
    pai[vertice] = vertice
    rank[vertice] = 0


def Find(vertice):
    if pai[vertice] != vertice:
        pai[vertice] = Find(pai[vertice])
    return pai[vertice]


def Union(vertice1, vertice2):
    raiz1 = Find(vertice1)
    raiz2 = Find(vertice2)
    if raiz1 != raiz2:
        if rank[raiz1] > rank[raiz2]:
            pai[raiz2] = raiz1
        else:
            pai[raiz1] = raiz2
        if rank[raiz1] == rank[raiz2]:
            rank[raiz2] += 1


def kruskal(G, w=None):
    for vertice in G['vertices']:
        makeSet(vertice)
        print('Constroi o conjunto unitário de {}'.format(vertice))
        arvoreGeradoraMinima = set()
        arestas = list(G['edges'])
        arestas.sort()

    for aresta in arestas:
        w, vertice1, vertice2 = aresta
        print('Testa se a raiz de {} e {} são diferentes'.format(vertice1, vertice2))
        if Find(vertice1) != Find(vertice2):
            print('A raizes de {} e {} são diferentes'.format(
                vertice1, vertice2))
            Union(vertice1, vertice2)
            print('Faz a união entre {} - {}'.format(vertice1, vertice2))
            arvoreGeradoraMinima.add(aresta)
            print('Adiciona aresta {} à arvore geradora mínima'.format(aresta))
        else:
            print('As raízes de {} e {} são iguais'.format(vertice1, vertice2))
            print('Raiz de {} é {}'.format(vertice1, Find(vertice1)))
            print('Raiz de {} é {}'.format(vertice2, Find(vertice2)))
    return sorted(arvoreGeradoraMinima)


grafo = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': set([
        (7, 'A', 'D'),
        (5, 'A', 'C'),
        (7, 'B', 'B'),
        (8, 'B', 'A'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'A'),
        (5, 'D', 'E'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (15, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F'),
    ])
}

print('Resultado: ', kruskal(grafo))
