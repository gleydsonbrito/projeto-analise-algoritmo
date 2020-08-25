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


#print(integerMultiplication(1234, 5678))


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


print(scheduleCompatibleTasks(Tasks))
