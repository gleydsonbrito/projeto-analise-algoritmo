import random as rnd
import matplotlib.pyplot as plt
import numpy as np

M = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]
M1 = M.copy()
M2 = M.copy()
M3 = M.copy()

P = [150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
P1 = P.copy()
P2 = P.copy()
P3 = P.copy()

A = rnd.sample(range(10, 100), 15)
A1 = A.copy()
A2 = A.copy()
A3 = A.copy()


def bubbleSort5Melhorado(A):
    # Como melhoramento fdoi utilizada a variável parteOrdenada
    # que diminui a verredura no FOR interno considerando a parte
    # já ordenada
    s = 0
    n = len(A) - 1
    ordenado = False
    parteOrdenada = 0
    while not ordenado:
        ordenado = True
        for i in range(n-parteOrdenada):
            s += 1
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                ordenado = False
        parteOrdenada = parteOrdenada + 1
    print('Passos: {}'.format(s))
    return A


def bubbleSort5(A):
    # Como melhoramento foi utilizada a variável parteOrdenada
    # o que diminui a verredura no FOR interno
    # considerando a parte já ordenada
    s = 0
    n = len(A) - 1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(n):
            s += 1
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                ordenado = False

    print('Passos: {}'.format(s))
    return A


def meuMetodoDeOrdenacao(A):
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
        for j in range(n-1-k, 0 + k, -1):
            s += 1
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                ordenado = False
        k = k + 1
    print("Passos: ", s)
    return A


print('\nBubblesort5')
print('Melhor caso: ', M1)
print('Resultado Ordenado: ', bubbleSort5(M1))

print('\nBubblesort5 - Melhorado')
print('Pior caso: ', P1)
print('Resultado Ordenado: ', bubbleSort5(P1))

print('\nBubblesort5 - Melhorado')
print('Lista aleatória: ', A1)
print('Resultado Ordenado: ', bubbleSort5(A1))

print('\n******************************************************')

print('\nBubblesort5 - Melhorado')
print('Melhor caso: ', M2)
print('Resultado Ordenado: ', bubbleSort5Melhorado(M2))

print('\nBubblesort5 - Melhorado')
print('Pior caso: ', P2)
print('Resultado Ordenado: ', bubbleSort5Melhorado(P2))

print('\nBubblesort5 - Melhorado')
print('Lista aleatória: ', A2)
print('Resultado Ordenado: ', bubbleSort5Melhorado(A2))

print('\n******************************************************')

print('\nMeu Método')
print('Melhor caso: ', M3)
print('Resultado Ordenado: ', meuMetodoDeOrdenacao(M3))

print('\nMeu Método')
print('Pior caso: ', P3)
print('Resultado Ordenado: ', meuMetodoDeOrdenacao(P3))

print('\nMeu Método')
print('Lista aleatória: ', A3)
print('Resultado Ordenado: ', meuMetodoDeOrdenacao(A3))
