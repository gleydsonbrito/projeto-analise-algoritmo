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


def dijkstra(D, s, p):
    visitado = {s: 0}
    path = {}

    V = set(D.vertice)
    print('Inicia pelo vertice {}'.format(s))
    while V:
        p += 1
        minimo = None
        for vert in V:
            p += 1
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
            p += 1
            try:
                peso = peso_atual + D.distancia[(minimo, y)]
            except:
                continue
            if y not in visitado or peso < visitado[y]:
                visitado[y] = peso
                path[y] = minimo
    print('Passos: {}'.format(p))
    return visitado, path


def caminho_minimo(D, s, destino, p):
    visitado, paths = dijkstra(D, s, p)
    caminho_total = deque()
    _destino = paths[destino]
    print('Caminho de {} até {}'.format(s, destino))

    while _destino != s:
        p += 1
        caminho_total.appendleft(_destino)
        _destino = paths[_destino]

    caminho_total.appendleft(s)
    caminho_total.append(destino)
    return visitado[destino], list(caminho_total)


dig = Digrafo()

for v in [1, 2, 3, 4, 5, 6, 7]:
    dig.adicionaVertice(v)

dig.adicionaArco(1, 2, 10)
dig.adicionaArco(1, 3, 20)
dig.adicionaArco(2, 4, 15)
dig.adicionaArco(3, 4, 30)
dig.adicionaArco(2, 5, 50)
dig.adicionaArco(4, 5, 30)
dig.adicionaArco(5, 6, 5)
dig.adicionaArco(6, 7, 2)

print('Custo mínimo: ', caminho_minimo(dig, 1, 5, 0))
