import random


def bubbleSort0(A, d=0):  # Melhor caso O(n²) e Pior caso O(n²)
    # Super ingênuo
    n = len(A)-1
    for i in range(n):
        for j in range(n):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]


def bubbleSort1(A, d=0):
    # bubble naive mas nem tanto
    n = len(A)-1
    for i in range(n):  # O(n)
        for j in range(0, n-i):
            if A[j] > A[j+1]:
                aux = A[j]
                A[j] = A[j+1]
                A[j+1] = aux


def bubbleSort2(A, d=0):
    # bubble com flag sem considerar parte ordenada
    n = len(A)
    for i in range(n-1):  # O(1) + O(n)
        flag = 0
        for j in range(n-1):
            if A[j] > A[j+1]:
                aux = A[j]
                A[j] = A[j+1]
                A[j+1] = aux
                flag = 1
        if flag == 0:
            break


def bubbleSort3(A, d=0):
    # bubble com flag considerando parte ordenada de forma naive
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


def bubbleSort4(A, d=0):
    # considerando parte já ordenada de forma inteligente
    n = len(A)
    while True:
        newn = 0  # O(n²)
        for j in range(n-1):
            if A[j] > A[j+1]:
                aux = A[j]
                A[j] = A[j+1]
                A[j+1] = aux
                newn = j
        n = newn+1
        if n <= 1:
            break


def bubbleSort5(A, d=0):
    # sem usar break mas naive como o 2,
    # pode ser melhorado usando técnicas do 1 ou do 4
    n = len(A) - 1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(n):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                ordenado = False
        n -= 1
