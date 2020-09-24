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

    def graMaximo(self,):
        max = 0
        graus = []
        for a in self.adjacencias:
            contador = 0
            aresta = a[0]
            while a[0] == aresta:
                contador += 1
            graus.append(contador)

        for m in graus:
            if max < m:
                max = m

        return print("Grau máximo: ", max)

    def grauMinimo(self,):
        min = 99999999
        for a in self.adjacencias:
            if min > len(a):
                min = len(a)
        return print("Grau Mínimo: ", min)


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
grafo.graMaximo()
grafo.grauMinimo()
