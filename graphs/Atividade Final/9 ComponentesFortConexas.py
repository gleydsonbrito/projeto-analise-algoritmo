from collections import defaultdict


class Grafo:
    def __init__(self, vertice):
        self.V = vertice
        self.grafo = defaultdict(list)

    # adiciona arestas no grafo
    def adicionarAresta(self, s, d):
        self.grafo[s].append(d)

    # busca em profundidade recursiva
    def dfs(self, d, verticeVisitado):
        # visita o vertice
        verticeVisitado[d] = True
        # faz uma busca em ordem na arvore de vertices
        print(d, end='')
        for i in self.grafo[d]:
            if not verticeVisitado[i]:
                self.dfs(i, verticeVisitado)

    def preenche_em_ordem(self, d, verticeVisitado, pilha):
        verticeVisitado[d] = True
        for i in self.grafo[d]:
            if not verticeVisitado[i]:
                self.preenche_em_ordem(i, verticeVisitado, pilha)
        pilha = pilha.append(d)

    def matrizTransposta(self):
        g = Grafo(self.V)

        for i in self.grafo:
            for j in self.grafo[i]:
                g.adicionarAresta(j, i)
        return g

    # imprimindo os componentes fortemente conexos
    def imprimeComponentesFortementeConexos(self):
        P = []
        verticesVisitados = [False] * (self.V)

        for i in range(self.V):
            if not verticesVisitados[i]:
                self.preenche_em_ordem(i, verticesVisitados, P)

        gr = self.matrizTransposta()

        verticesVisitados = [False] * (self.V)

        while P:
            i = P.pop()
            if not verticesVisitados[i]:
                gr.dfs(i, verticesVisitados)
                print("")


g = Grafo(9)
g.adicionarAresta(1, 2)
g.adicionarAresta(2, 3)
g.adicionarAresta(3, 4)
g.adicionarAresta(3, 5)
g.adicionarAresta(4, 1)
g.adicionarAresta(5, 6)
g.adicionarAresta(6, 7)
g.adicionarAresta(7, 5)
g.adicionarAresta(7, 8)

print("Strongly Connected Components:")
g.imprimeComponentesFortementeConexos()
