import xml.etree.ElementTree as et

tree = et.parse('brazil58.xml')
root = tree.getroot()


class Vertex:
    def __init__(self, vertex, _edges):
        self.vertex = vertex
        self._edges = _edges


class Edge:
    def __init__(self, city, distance):
        self.city = city
        self.distance = distance


# print(root[0][0].text)
graph = []


def createGraphByXMLFile():
    i = 1
    _vertex = None
    for k in range(len(root)):
        _edg = []
        for child in root[i-1]:
            n = 0
            n = n+1
            if n == i:
                n = n+1

            edge = Edge(
                'City: {}'.format(n),
                int(float(child.attrib['cost']))
            )

            _edg.append(edge)
            _vertex = Vertex(
                "City-{}".format(i),
                _edg
            )

        i = i + 1
        graph.append(_vertex)


createGraphByXMLFile()

for vertex in graph:
    print(vertex.vertex)
    for edge in vertex._edges:
        print(edge.city, edge.distance)


grafo = [
    {'cidade': 'a', 'adjacencias': [{'cidade': 'b', 'dist': 2713}, {'cidade': 'c', 'dist': 2437}, {
        'cidade': 'd', 'dist': 1234}, {'cidade': 'e', 'dist': 223}]},
    {'cidade': 'b', 'adjacencias': [{'cidade': 'a', 'dist': 2713}, {'cidade': 'c', 'dist': 654}, {
        'cidade': 'd', 'dist': 1256}, {'cidade': 'e', 'dist': 987}]},
    {'cidade': 'c', 'adjacencias': [{'cidade': 'a', 'dist': 1234}, {'cidade': 'b', 'dist': 654}, {
        'cidade': 'd', 'dist': 2437}, {'cidade': 'e', 'dist': 876}]},
    {'cidade': 'd', 'adjacencias': [{'cidade': 'a', 'dist': 1234}, {'cidade': 'b', 'dist': 1256}, {
        'cidade': 'c', 'dist': 2437}, {'cidade': 'e', 'dist': 3456}]},
    {'cidade': 'e', 'adjacencias': [{'cidade': 'a', 'dist': 223}, {'cidade': 'b', 'dist': 987}, {
        'cidade': 'c', 'dist': 876}, {'cidade': 'd', 'dist': 3456}]},
]


class Arvore:
    def __init__(self, vertice, visitado, predecessor):
        self.vertice = vertice
        self.visitado = visitado
        self.predecessor = predecessor


arvoreDeVertices = []

for vertice in grafo:
    arvoreDeVertices.append(Arvore(vertice, 0, None))
