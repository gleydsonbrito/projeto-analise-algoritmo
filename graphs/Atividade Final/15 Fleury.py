from collections import defaultdict


class Digrafo:
    def __init__(self, vertices):
        self.V = vertices
        self.digrafo = defaultdict(list)
        self.Time = 0

    # adiciona uma aresta ao digrafo
    def adicionaArco(self, u, v):
        self.digrafo[u].append(v)
        self.digrafo[v].append(u)

    # remove uma aresta do digrafo
    def removerArco(self, u, v):
        for indice, k in enumerate(self.digrafo[u]):
            if k == v:
                self.digrafo[u].pop(indice)
        for indice, k in enumerate(self.digrafo[v]):
            if k == u:
                self.digrafo[v].pop(indice)

    # função que conta os vertices alcançáveis de v
    def contaVerticesAlcancaveis(self, v, visitado):
        count = 1
        visitado[v] = True
        for i in self.digrafo[v]:
            if visitado[i] == False:
                count = count + self.contaVerticesAlcancaveis(i, visitado)
        return count

    # Checa se o arco u-v pode ser considerado proximo arco valido
    def arcoValido(self, u, v):
        if len(self.digrafo[u]) == 1:
            return True
        else:
            visitado = [False]*(self.V)
            verticesAlcancaveis1 = self.contaVerticesAlcancaveis(u, visitado)

            self.removerArco(u, v)
            visitado = [False]*(self.V)
            verticeAlcancaveis2 = self.contaVerticesAlcancaveis(u, visitado)

            # adiciona aresta de volta ao digrafo
            self.adicionaArco(u, v)

            return False if verticesAlcancaveis1 > verticeAlcancaveis2 else True

    def funcaoSuporte(self, u):
        for v in self.digrafo[u]:
            if self.arcoValido(u, v):
                print("%d-%d " % (u, v), end='-> '),
                self.removerArco(u, v)
                self.funcaoSuporte(v)

    def imprimir(self):
        # Encontra um vertice com grau impar
        u = 0
        for i in range(self.V):
            if len(self.digrafo[i]) % 2 != 0:
                u = i
                break
        self.funcaoSuporte(u)


dig = Digrafo(5)
dig.adicionaArco(1, 0)
dig.adicionaArco(0, 2)
dig.adicionaArco(2, 1)
dig.adicionaArco(0, 3)
dig.adicionaArco(3, 4)
dig.adicionaArco(3, 2)
dig.adicionaArco(3, 1)
dig.adicionaArco(2, 4)

print('Trilha Euleriana: ')
dig.imprimir()
