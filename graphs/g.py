class Grafo:
    def __init__(self,):
        self.vertices = []
        self.adjacencias = []

    def imprimirGrafo(self, ):
        print('Vertices: ')
        for v in self.vertices:
            print(v, end='-> ')
        print('Fim')
        print('Lista de adjacencias:')
        for a in self.adjacencias:
            print('('+str(a), end=') ')
        print('Fim')

    def addVertice(self, v):
        self.vertices.append(v)

    def addAdjacencias(self, a):
        self.adjacencias.append(a)

    def grau(self, opcao):
        graus = []
        for v in self.vertices:
            m = 0
            for i in range(len(self.adjacencias)):
                if v == self.adjacencias[i][0]:
                    m = m + 1
            graus.append(m)
        if opcao == 'max':
            return print("Grau máximo: ", max(graus))
        elif opcao == 'min':
            return print('Grau mínimo: ', min(graus))
        else:
            return print('Opção Inválida.')


grafo = Grafo()
grafo.addVertice(1)
grafo.addVertice(2)
grafo.addVertice(3)
grafo.addVertice(4)
grafo.addVertice(5)
grafo.addVertice(6)

grafo.addAdjacencias([1, 2])
grafo.addAdjacencias([1, 5])
grafo.addAdjacencias([1, 3])
grafo.addAdjacencias([2, 3])
grafo.addAdjacencias([2, 5])
grafo.addAdjacencias([3, 4])
grafo.addAdjacencias([3, 5])
grafo.addAdjacencias([3, 1])
grafo.addAdjacencias([4, 5])
grafo.addAdjacencias([4, 6])
grafo.addAdjacencias([5, 3])
grafo.addAdjacencias([5, 3])
grafo.addAdjacencias([5, 1])
grafo.addAdjacencias([6, 4])


grafo.imprimirGrafo()
grafo.grau('max')
grafo.grau('min')
