import math
# Algoritmo 18.1: MultiplicaInteiros(x, y, n)
# função que multiplica inteiros recursivamente


def integerMultiplication(x, y, n=4):
    # checa se o número não pode mais ser dividido e estabelece a condição de parada
    if n == 1:
        return x*y
    else:
        # função que separa os algarismos dos números
        ab = separateNumbers(x)
        cd = separateNumbers(y)

        # faz a chamada recurvida dividindo os algarismos por 2
        p1 = integerMultiplication(ab[0], cd[0], n/2)
        p2 = integerMultiplication(ab[0], cd[1], n/2)
        p3 = integerMultiplication(ab[1], cd[0], n/2)
        p4 = integerMultiplication(ab[1], cd[1], n/2)

    return math.pow(10, n) * p1 + math.pow(10, n/2) * (p2 + p3) + p4

# Algoritmo 18.2: karatsuba(x, y, n)


def karatsuba(x, y, n=4):
    # checa se o número não pode mais ser dividido e estabelece a condição de parada
    if n == 1:
        return x*y
    else:
        # função que separa os algarismos dos números
        ab = separateNumbers(x)
        cd = separateNumbers(y)

        # faz a chamada recursiva dividindo os algarismos por 2
        p1 = karatsuba(ab[0], cd[0], n/2)
        p2 = karatsuba(ab[0], cd[1], n/2)
        p3 = karatsuba(ab[0]+ab[1], cd[0]+cd[1], (n/2))

        return math.pow(10, n) * p1 + math.pow(10, n/2) * (p3 - p1 - p2) + p2


def separateNumbers(n):
    # converte o numero em string
    nString = str(n)
    # pega o tamanho da string
    tam = int(len(nString)/2)

    # pega o primeiro e segundo trecho baseado no tamanho
    a = int(nString[0:tam])
    b = int(nString[tam:int(len(nString)+1)])

    # retorna um array de inteiros
    return [int(a), int(b)]


# print(integerMultiplication(1234, 5678))


# algoritmo 19.1 EscalonamentoCompatível(T, n)
# Classe que modela uma tarefa com tempos iniciais e finais
class Task:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return str(self.start)+" - "+str(self.end)


# inicializando uma lista de tarefas
Tasks = [
    Task(2, 5),
    Task(0, 4),
    Task(1, 6),
    Task(5, 7),
    Task(3, 9),
    Task(1, 4),
    Task(5, 9),
    Task(6, 10),
    Task(8, 11),
    Task(8, 12),
    Task(12, 16),
]

# definindo um bubblesort para ordenar as tarefas pelo tempo final T[i].end


def sortTasksByEndTime(T):
    n = len(T)
    for j in range(n - 1):
        for i in range(n - 1):
            # ordena pelo tempo final
            if T[i].end > T[i + 1].end:
                aux = T[i]
                T[i] = T[i+1]
                T[i + 1] = aux
    return T

# implementa o escalonamento de tarefas compatíveis


def scheduleCompatibleTasks(T, n=None):
    # pega o tamando da lista de entrada
    n = len(T)
    # inicializa uma lista vazia de tarefas compatíveis
    S = []
    # ordena a lista de tarefas
    T = sortTasksByEndTime(T)
    # pega o primeiro elemento e insere na listas S de tarefas compatíveis
    S.append(T[0])
    # guarda a posição da última tarefa adicionada
    k = 1
    # indice para o for
    i = 1
    # pega as tarefas compatíveis que iniciam logo após a anterior
    for i in range(i, n):
        if T[i].start >= T[k].end:
            S.append(T[i])
            k = i

    return S

# Saída com as tarefas compatíveis
# print(scheduleCompatibleTasks(Tasks))


# Problema da mochila fracinária, algoritmo 19.2
# define a classe item da mochila, com valor, peso e razão valor/peso


class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.rationVW = value/weight

    def __repr__(self):
        return str(self.value)+"-"+str(self.weight)

# usa o bubble sort para ordenar pelo razão do valor/peso


def sortItmesByRation(I):
    n = len(I)
    for j in range(n - 1):
        for i in range(n - 1):
            # ordena pela razão valor/peso
            if I[i].rationVW < I[i + 1].rationVW:
                aux = I[i]
                I[i] = I[i+1]
                I[i + 1] = aux
    return I


# define uma lista de itens com seus respectivos valores e pesos
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
# capacidade de peso total da mochima
W = 50

# define a função que argupa os itens na mochila


def fractionalKnapsackProblem(I, W, n=None):
    # ordena os itens pela razão valor/peso
    I = sortItmesByRation(I)
    # inicializa o i
    i = 0
    # pega o tamanho da lista de itens
    n = len(I)
    # define um array de quantidade de itens da mochila
    f = [0, 0, 0]
    # pega a capacidade da mochila
    capacit = W

    # percorre a lista ordenada pelo peso e coloca os itens inteiros na mochina
    # enquanto ainda há capacidade
    while i < n and capacit >= I[i].weight:
        # caso haja capacidade, insere um item inteiro na mochila
        f[i] = 1
        # reduz a capacidade da mochila de acordo com o peso colocado
        capacit = capacit - I[i].weight
        # caminha na lista de itens
        i = i + 1

    # quando não há mais capacidade na mochila
    # pega a posição atual e adiciona no vetoro de quantidades f
    # o valor do peso que a mochila ainda comporta, que neste caso a mochila
    # não comporta mais um intem inteiro, apenas uma fração dele
    if i < n:
        f[i] = capacit/I[i].weight

    # a partir dauqui a mochila não comporta mais itens
    # então o vetor de quantidades é preenchido com 0 (zeros)
    # para informar que nenhum item mais entrou na mochila
    j = i + 1
    for j in range(j, n):
        f[j] = 0

    # retorna a lista que informar quanto de cada item foi adicionado a mochila
    return f


# imprime o vetor f
# print(fractionalKnapsackProblem(items, W))
# saída [1, 1, 0.6666666666666666]

# Algoritmo 19.3: HUFFMAN(A,f)
string = "BANANA"


# implementação do oibjeto nó
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffmanTree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffmanTree(l, True, binString + '0'))
    d.update(huffmanTree(r, False, binString + '1'))
    return d


# calcula frequência de cada caracter da palavra
freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

# ordena a lista na ordem inversa da frequência(menor => maior)
freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]  # recupera último elemento
    (key2, c2) = nodes[-2]  # recupera o penúltimo elemento
    nodes = nodes[:-2]  # remove os dois últimos elementos
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffmanTree(nodes[0][0])

print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffmanCode[char]))
