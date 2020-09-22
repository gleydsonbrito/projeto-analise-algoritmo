grafo = [
    {'cidade': 'a', 'adjacencias': [
        {'cidade': 'b', 'dist': 2713}, {'cidade': 'c', 'dist': 2437}]},
    {'cidade': 'b', 'adjacencias': [
        {'cidade': 'a', 'dist': 2713}, {'cidade': 'c', 'dist': 654}, ]},
    {'cidade': 'c', 'adjacencias': [{'cidade': 'a', 'dist': 1234}, {'cidade': 'b', 'dist': 654}, {
        'cidade': 'd', 'dist': 2437}]}, {'cidade': 'd', 'adjacencias': [{'cidade': 'a', 'dist': 1234}, {'cidade': 'b', 'dist': 1256}, {
            'cidade': 'c', 'dist': 2437}, {'cidade': 'e', 'dist': 3456}]},
    {'cidade': 'e', 'adjacencias': [
        {'cidade': 'a', 'dist': 223}, {'cidade': 'b', 'dist': 987}]},
]

# for cidade in grafo:
#   print(cidade['cidade'])
#  for ed in cidade['adjacencias']:
#     print(ed['cidade'], ed['dist'])


def grauMaximo(grafo):
    max = 0
    for cidade in grafo:
        vizinhanca = len(cidade['adjacencias'])
        if vizinhanca > max:
            max = vizinhanca
    return max


print('Grau Máximo: ', grauMaximo(grafo))


def grauMinimo(grafo):
    min = 99999
    for cidade in grafo:
        vizinhaca = len(cidade['adjacencias'])
        if vizinhaca < min:
            min = vizinhaca
    return min


print('Grau Mínimo: ', grauMinimo(grafo))


class Arvore:
    def __init__(self, vertice, visitado, predecessor):
        self.vertice = vertice
        self.visitado = visitado
        self.predecessor = predecessor


arvoreDeVertices = []

for vertice in grafo:
    arvoreDeVertices.append(Arvore(vertice, 0, None))
