import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
M = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
P = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
A = random.sample(range(10, 100), 15)


def bubbleSort0(A, d=0):  # Melhor caso O(n²) e Pior caso O(n²)
    # Super ingênuo
    s = 0
    n = len(A)-1
    for i in range(n):
        for j in range(n):
            s += 1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    print('Passos: {}'.format(s))
    return A


def bubbleSort1(A, d=0):
    # bubble naive mas nem tanto
    s = 0
    n = len(A)-1
    for i in range(n):  # O(n)
        for j in range(0, n-i):
            s += 1
            if A[j] > A[j+1]:
                aux = A[j]
                A[j] = A[j+1]
                A[j+1] = aux
    print('Passos: {}'.format(s))
    return A


def bubbleSort2(A, d=0):
    # bubble com flag sem considerar parte ordenada
    s = 0
    n = len(A)
    for i in range(n-1):  # O(1) + O(n)
        flag = 0
        for j in range(n-1):
            s += 1
            if A[j] > A[j+1]:
                aux = A[j]
                A[j] = A[j+1]
                A[j+1] = aux
                flag = 1
        if flag == 0:
            break
    print('Passos: {}'.format(s))
    return A


def bubbleSort3(A, d=0):
    # bubble com flag considerando parte ordenada de forma naive
    s = 0
    n = len(A)
    for i in range(n-1):  # melhor caso O(1) + O(n)
        flag = 0
        for j in range(n-1):  # pior caso (n²)
            if A[j] > A[j+1]:
                aux = A[j]
                A[j] = A[j+1]
                A[j+1] = aux
                flag = 1
        n -= 1  # otimização
        if flag == 0:
            break
    print('Passos: {}'.format(s))
    return A


def bubbleSort4(A, d=0):
    # considerando parte já ordenada de forma inteligente
    s = 0
    n = len(A)
    while True:
        newn = 0  # O(n²)
        for j in range(n-1):
            s += 1
            if A[j] > A[j+1]:
                aux = A[j]
                A[j] = A[j+1]
                A[j+1] = aux
                newn = j
        n = newn+1
        if n <= 1:
            break
    print('Passos: {}'.format(s))
    return A


def bubbleSort5(A, d=0):
    # sem usar break mas naive como o 2,
    # pode ser melhorado usando técnicas do 1 ou do 4
    s = 0
    n = len(A) - 1
    ordenado = False
    while not ordenado:
        ordenado = True
        parteOrdenada = 0
        for i in range(n-parteOrdenada):
            s += 1
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                ordenado = False
        parteOrdenada = parteOrdenada + 1
    print('Passos: {}'.format(s))
    return A


def bubbleSort6(A):
    s = 0
    n = len(A) - 1
    k = 0
    ordenado = False
    while ordenado is False:
        ordenado = True
        for i in range(k, n-k):
            s += 1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                ordenado = False
        j = n - k
        for j in range(n-k, 0 + k, -1):
            s += 1
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                ordenado = False
        k = k + 1
    print(s)
    return s


"""
ref = []
casos = []

for r in range(0, 50):
    aleatorio = random.sample(range(10, 100), 15)
    ret = bubbleSort6(aleatorio)
    casos.append(ret)
    ref.append(r+1)


print(min(casos))
print(max(casos))
print(np.mean(casos))

plt.plot(ref, casos)
plt.xlabel('Número de elementos')
plt.ylabel('Número de execuções')
plt.show()
"""
