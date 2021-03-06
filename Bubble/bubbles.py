
# Em todos os algoritmos o parametro d é de debug naive
# d=0, sem debug. d=1, com.

import random


def bubbleSort0(A, d=0):
    # Super ingênuo
    n = len(A)-1
    s = 0
    c = " "
    for i in range(n):  # O(n)
        for j in range(n):  # O(n)
            s += 1
            if d:
                print(A)
            if A[j] > A[j+1]:
                if d:
                    m = (2*c)+"|"+(2*c)
                    l = (j)*(4*c)+m+(n-j-len(m))*(4*c)
                    print(l)
                    print(j)
                A[j], A[j+1] = A[j+1], A[j]
    print(s, " passos")


def bubbleSort1(A, d=0):
    # bubble naive mas nem tanto
    n = len(A)-1
    s = 0
    c = " "
    for i in range(n):  # O(n)
        for j in range(0, n-i):
            s += 1
            if d:
                print(A)
            if A[j] > A[j+1]:
                if d:
                    m = (2*c)+"|"+(2*c)
                    l = (j)*(4*c)+m+(n-j-len(m))*(4*c)
                    print(l)
                    print(j)
                aux = A[j]
                A[j] = A[j+1]
                A[j+1] = aux
    print(s, " passos")

# Em todos os algoritmos o parametro d é de debug naive
# d=0, sem debug. d=1, com.


def bubbleSort0(A, d=0):
    # Super ingênuo
    n = len(A)-1
    s = 0
    c = " "
    for i in range(n):
        for j in range(n):
            s += 1
            if d:
                print(A)
            if A[j] > A[j+1]:
                if d:
                    m = (2*c)+"|"+(2*c)
                    l = (j)*(4*c)+m+(n-j-len(m))*(4*c)
                    print(l)
                    print(j)
                A[j], A[j+1] = A[j+1], A[j]
    print(s, " passos")


def bubbleSort1(A, d=0):
    # bubble naive mas nem tanto
    n = len(A)
    s = 0
    c = " "
    for i in range(n-1):
        for j in range(0, n-i-1):
            s += 1
            if d:
                print(A)
            if A[j] > A[j+1]:
                if d:
                    m = (2*c)+"|"+(2*c)
                    l = (j)*(4*c)+m+(n-j-len(m))*(4*c)
                    print(l)
                    print(j)
                aux = A[j]
                A[j] = A[j+1]
                A[j+1] = aux
    print(s, " passos")


def bubbleSort2(A, d=0):
    # bubble com flag sem considerar parte ordenada
    n = len(A)
    s = 0
    c = " "
    for i in range(n-1):
        flag = 0
        for j in range(n-1):
            s += 1
            if d:
                print(A)
            if A[j] > A[j+1]:
                if d:
                    m = (2*c)+"|"+(2*c)
                    l = (j)*(4*c)+m+(n-j-len(m))*(4*c)
                    print(l)
                    print(j)
                aux = A[j]
                A[j] = A[j+1]
                A[j+1] = aux
                flag = 1
        if flag == 0:
            break
    print(s, " passos")


def bubbleSort3(A, d=0):
    # bubble com flag considerando parte ordenada de forma naive
    n = len(A)
    s = 0
    c = " "
    for i in range(n-1):
        flag = 0
        for j in range(n-1):
            s += 1
            if d:
                print(A)
            if A[j] > A[j+1]:
                if d:
                    m = (2*c)+"|"+(2*c)
                    l = (j)*(4*c)+m+(n-j-len(m))*(4*c)
                    print(l)
                    print(j)
                aux = A[j]
                A[j] = A[j+1]
                A[j+1] = aux
                flag = 1
        n -= 1
        if flag == 0:
            break
    print(s, " passos")


def bubbleSort4(A, d=0):
    # considerando parte já ordenada de forma inteligente
    n = len(A)
    s = 0
    c = " "
    while True:
        newn = 0
        for j in range(n-1):
            s += 1
            if d:
                print(A)
            if A[j] > A[j+1]:
                if d:
                    m = (2*c)+"|"+(2*c)
                    l = (j)*(4*c)+m+(n-j-len(m))*(4*c)
                    print(l)
                    print(j)
                aux = A[j]
                A[j] = A[j+1]
                A[j+1] = aux
                newn = j
        n = newn+1
        if n <= 1:
            break
    print(s, " passos")


def bubbleSort5(A, d=1):
    # sem usar break mas naive como o 2,
    # pode ser melhorado usando técnicas do 1 ou do 4
    n = len(A) - 1
    s = 0
    c = " "
    ordenado = False
    k = 0
    while not ordenado:
        ordenado = True
        for i in range(n-k):
            s += 1
            if d:
                print(A)
            if A[i] > A[i + 1]:
                if d:
                    m = (2*c)+"|"+(2*c)
                    l = (i)*(4*c)+m+(n-i-len(m))*(4*c)
                    print(l)
                    print(i)
                A[i], A[i + 1] = A[i + 1], A[i]
                ordenado = False
        k = k+1
    print(s, " passos")


print("Caso aleatório")
w = random.sample(range(10, 100), 15)
print(w)
s = w.copy()
print('Sort-0')
bubbleSort0(s)
s = w.copy()
print('Sort-1')
bubbleSort1(s)
s = w.copy()
print('Sort-2')
bubbleSort2(s)
s = w.copy()
print('Sort-3')
bubbleSort3(s)
s = w.copy()
print('Sort-4')
bubbleSort4(s)
s = w.copy()
print('Sort-5')
bubbleSort5(s)
print(w)
print("Pior caso")
w = list(range(150, 0, -10))
print(w)
s = w.copy()
print('Sort-0')
bubbleSort0(s)
s = w.copy()
print('Sort-1')
bubbleSort1(s)
s = w.copy()
print('Sort-2')
bubbleSort2(s)
s = w.copy()
print('Sort-3')
bubbleSort3(s)
s = w.copy()
print('Sort-4')
bubbleSort4(s)
s = w.copy()
print('Sort-5')
bubbleSort5(s)
print("Melhor caso")
w = list(range(10, 160, 10))
print(w)
s = w.copy()
print('Sort-0')
bubbleSort0(s)
s = w.copy()
print('Sort-1')
bubbleSort1(s)
s = w.copy()
print('Sort-2')
bubbleSort2(s)
s = w.copy()
print('Sort-3')
bubbleSort3(s)
s = w.copy()
print('Sort-4')
bubbleSort4(s)
s = w.copy()
print('Sort-5')
bubbleSort5(s)
