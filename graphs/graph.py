from collections import deque


class Vertex:
    def __init__(self, n, visitado=False):
        self.n = n
        self.visitado
# classe que define o grafo
# constituido de uma lista de vértices e uma lista de arestas
# o vertice é representado por um número inteiro
# a aresta por um arrau de 2 posições [a, b] com A e B inteiros


class Grafo:
    def __init__(self,):
        self.vertices = []
        self.arestas = []
    # imprime o grafo

    def imprimirGrafo(self, ):
        # pecorre a lista de vétices imprimindo um a um
        for v in self.vertices:
            print(v, end='-> ')
        print('*')
        # percorre a lista de arestas imprimindo um a um
        for a in self.arestas:
            print('('+str(a), end=') ')
        print('*')

    def addVertice(self, v):  # adiciona vértice ao grafo
        self.vertices.append(v)

    def addArestas(self, a):  # adiciona uma aresta ao grafo
        self.arestas.append(a)

    # calcula o grau do vértice
    # recebe a opão 'max' ou 'min' como parâmetro de entrada
    def grau(self, opcao):
        # lista de graus de todos os vértices
        # o valor de grau[0..1..n] contém o grau desse vértice, etc...
        graus = []
        # percorre a lista de vértices
        for v in self.vertices:
            # acumulador do grau do vértice em questão
            grauDeV = 0
            # percorre a lista de arestas
            for i in range(len(self.arestas)):
                # se o vértice v for igual a aresta[0] acumula um em grauDeV
                if v == self.arestas[i][0]:
                    grauDeV = grauDeV + 1
            # insere o grau na lista de graus
            graus.append(grauDeV)
        # avalia o parâmetro de entrada, max retorna o máximo, e vice versa...
        if opcao == 'max':
            return print("Grau máximo: ", max(graus))
        elif opcao == 'min':
            return print('Grau mínimo: ', min(graus))
        else:
            return print('Opção Inválida.')

    def exlcuirVertice(self, vert):
        index = -1
        for i in range(len(self.vertices)):
            if self.vertices[i] == vert:
                index = i
        del self.vertices[index]

    def BuscaEmLargura(self, s, G=None):
        s.visitado = True
        F = deque()
        F.append(s)
        while len(F) > 0:
            u = F.popleft()


# cria uma instância vazia do grafo
grafo = Grafo()
# adiciona vértices (números inteiros)
grafo.addVertice(Vertex(1))
grafo.addVertice(Vertex(2))
grafo.addVertice(Vertex(3))
grafo.addVertice(Vertex(4))
grafo.addVertice(Vertex(5))
grafo.addVertice(Vertex(6))
# adiciona as arestas um array de 2 números inteiros, atesta [a, b]...
grafo.addArestas([1, 2])
grafo.addArestas([1, 5])
grafo.addArestas([1, 3])
grafo.addArestas([2, 3])
grafo.addArestas([2, 5])
grafo.addArestas([3, 4])
grafo.addArestas([3, 5])
grafo.addArestas([3, 1])
grafo.addArestas([4, 5])
grafo.addArestas([4, 6])
grafo.addArestas([5, 3])
grafo.addArestas([5, 3])
grafo.addArestas([5, 1])
grafo.addArestas([6, 4])

# imprime o grafo
grafo.imprimirGrafo()
# imprime os graus
grafo.grau('max')
grafo.grau('min')

grafo.exlcuirVertice(2)

grafo.imprimirGrafo()
