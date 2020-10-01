class G:

    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    # Adiciona arestas
    def adiciona_arestas(self, s, d, w):
        self.grafo.append([s, d, w])

    # imprime a soluação
    def imprimir(self, dist, s):
        print("Distância da fonte a todos os vértices")
        for i in range(self.V):
            if dist[i] == float('inf'):
                dist[i] = 'Não há caminho'
            print('Distâncicia de {} até {} = {}'.format(s, i, dist[i]))

    def bellman_ford(self, vertice_fonte):
        # Preenchendo o array de distânia e de predecessores
        distancia = [float("Inf")] * self.V

        # marca o vértice fonte
        distancia[vertice_fonte] = 0

        # Relaxamento das arestas
        for _ in range(self.V - 1):
            for s, d, w in self.grafo:
                print('Origiem {} -> destino {} -> e distâncica {}'.format(s, d, w))
                if distancia[s] != float("Inf") and distancia[s] + w < distancia[d]:
                    distancia[d] = distancia[s] + w

        # Detectando ciclos negativos
        # se o velor muda então temos um ciclo negativo
        # e não podemos encontrar o menor caminho

        for s, d, w in self.grafo:
            if distancia[s] != float("Inf") and distancia[s] + w < distancia[d]:
                print("O digrafo contém ciclos negativos")
                return

        # Se nenhum ciclo foi encontrado
        # Imprime a distância e o array predecessor
        self.imprimir(distancia, vertice_fonte)


g = G(5)
g.adiciona_arestas(0, 1, 5)
g.adiciona_arestas(0, 2, 4)
g.adiciona_arestas(1, 3, 3)
g.adiciona_arestas(2, 1, 6)
g.adiciona_arestas(3, 2, 2)

g.bellman_ford(3)
