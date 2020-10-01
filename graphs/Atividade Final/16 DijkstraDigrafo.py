from collections import defaultdict, deque


class Digrafo(object):
    def __init__(self):
        self.vertice = set()
        self.arcos = defaultdict(list)
        self.distancia = {}

    def adicionaVertice(self, v):
        self.vertice.add(v)

    def adicionaArco(self, u, v, dist):
        self.arcos[u].append(v)
        self.arcos[v].append(u)
        self.distancia[(u, v)] = dist


def dijkstra(D, s):
    visitado = {s: 0}
    path = {}

    V = set(D.vertice)
    print('Inicia pelo vertice {}'.format(s))
    while V:
        minimo = None
        for vert in V:
            print('Verifica se {} já foi visitado ?'.format(vert))
            if vert in visitado:
                print('Visitando {}'.format(vert))
                if minimo is None:
                    minimo = vert
                    print('Adiciona {}'.format(minimo))
                elif visitado[vert] < visitado[minimo]:
                    minimo = vert
            print('Segue para o próximo vertice')
        if minimo is None:
            break

        V.remove(minimo)
        peso_atual = visitado[minimo]
        print("Peso total {}".format(visitado[minimo]))

        for y in D.arcos[minimo]:
            try:
                peso = peso_atual + D.distancia[(minimo, y)]
            except:
                continue
            if y not in visitado or peso < visitado[y]:
                visitado[y] = peso
                path[y] = minimo

    return visitado, path


def caminho_minimo(D, s, destino):
    visitado, paths = dijkstra(D, s)
    caminho_total = deque()
    _destino = paths[destino]
    print('Caminho de {} até {}'.format(s, destino))

    while _destino != s:
        caminho_total.appendleft(_destino)
        _destino = paths[_destino]

    caminho_total.appendleft(s)
    caminho_total.append(destino)

    return visitado[destino], list(caminho_total)


dig = Digrafo()

for v in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    dig.adicionaVertice(v)

dig.adicionaArco('A', 'B', 10)
dig.adicionaArco('A', 'C', 20)
dig.adicionaArco('B', 'D', 15)
dig.adicionaArco('C', 'D', 30)
dig.adicionaArco('B', 'E', 50)
dig.adicionaArco('D', 'E', 30)
dig.adicionaArco('E', 'F', 5)
dig.adicionaArco('F', 'G', 2)

print('Custo mínimo: ', caminho_minimo(dig, 'A', 'E'))
