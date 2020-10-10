class Grafo:
    def __init__(self, v):
        self.vertices = v
        self.adjacencias = [[] for i in range(v)]

    def adicionaAresta(self, u, v):
        print('Adiciona a aresta {}-{}'.format(u, v))
        self.adjacencias[u].append(v)

    def ordenacaoTopologica(self, s, visitado):
        p=0
        visitado[s] = True
        print('Visitando {}'.format(s))
        for u in self.adjacencias[s]:
            p+=1
            if not visitado[u]:
                self.ordenacaoTopologica(u, visitado)
        self.S.append(s)
        print('Passos: {}'.format(p))
        print('Insere {} na ordem'.format(s))

    def imprimirGrafo(self):
        visitado = [False]*self.vertices
        self.S = []
        for i in range(self.vertices):
            if not visitado[i]:
                self.ordenacaoTopologica(i, visitado)
        print('Ordem Topológica: ', self.S)


G = Grafo(5)
G.adicionaAresta(0, 1)
G.adicionaAresta(0, 3)
G.adicionaAresta(0, 4)
G.adicionaAresta(1, 2)
G.adicionaAresta(4, 2)
G.adicionaAresta(3, 4)
G.imprimirGrafo()
