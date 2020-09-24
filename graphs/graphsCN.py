grafo = [
    {'cidade': 'a', 'adjacencias': [
        {'cidade': 'b', 'dist': 2713}, {'cidade': 'c', 'dist': 2437}]},
    {'cidade': 'b', 'adjacencias': [
        {'cidade': 'a', 'dist': 2713}, {'cidade': 'c', 'dist': 654}, ]},
    {'cidade': 'c', 'adjacencias': [{'cidade': 'a', 'dist': 1234}, {'cidade': 'b', 'dist': 654}, {
        'cidade': 'd', 'dist': 2437}]},
    {'cidade': 'd', 'adjacencias': [{'cidade': 'a', 'dist': 1234}, {'cidade': 'b', 'dist': 1256}, {
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


def getIndex(G, s):
    index = -1
    for i in range(len(G)):
        if G[i]['cidade'] == s:
            index = i
    return index


def getAdjacencias(index, G):
    return G[index]['adjacencias']


def imprimirGrafo(G):
    for c in G:
        print(c['cidade'], end='-> '),


def removeVerticesAdjacentesDeSEmG(G, s):
    for v in G:
        for i in range(len(v['adjacencias'])):
            if v['adjacencias'][i]['cidade'] == s:
                del v['adjacencias'][i]


def busca(G, s):
    T = [{'cidade': s, 'adjacencias': []}]
    index = getIndex(G, s)
    removeVerticesAdjacentesDeSEmG(G, s)
    i = 0
    del G[index]
    for v in G:
        for e in v['adjacencias']:
            if e['cidade'] == T[i]['cidade']:
                T.append({'cidade': e['cidade'], "adjacencias": []})
                #del G[getIndex(e['cidade'])]

    return T


# resultado
g = busca(grafo, 'd')
