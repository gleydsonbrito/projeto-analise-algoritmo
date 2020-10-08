import random
import matplotlib.pyplot as plt
import pandas as pd


def bubble(A):
    s = 0
    n = len(A)-1
    for i in range(0, n):
        for j in range(0, n):
            s += 1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    #print('Número de exceuções Bubblesort Puro: {}'.format(s))
    return s


def bubble_v2(A):
    s = 0
    n = len(A)-1
    k = n
    for i in range(0, n):
        for j in range(0, k):
            s += 1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            k -= 1
    # k controla a ultimna posição do vetor, que sempre apos a primeira passagem
    # conterá o elemento de maior valor  Então diminuir esse k otimiza as buscas
    # drasticamente. Bubble_otrimizado!
    #print('Número de exceuções Bubblesort Otimizado: {} '.format(s))
    return s


ite = 10
A = random.sample(range(10, 200), ite)
A2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

res = []
b_v1 = []
b_v2 = []
for k in range(10):
    res.append(ite)
    b_v1.append(bubble(A))
    b_v2.append(bubble_v2(A))
    ite = ite + 10
    A = random.sample(range(10, 200), ite)
"""
data = {}
for i in range(0, len(res)):
    data.update({i: [int(b_v1[i]), int(b_v2[i])]})

df = pd.DataFrame(data, columns=[1, 2])

df.plot()
plt.show()
"""
"""
plt.plot(res, b_v1)
plt.xlabel('Número de elementos')
plt.ylabel('Número de execuções')
plt.ylim(0, 10000)
plt.show()

plt.plot(res, b_v2)
plt.xlabel('Número de elementos')
plt.ylabel('Número de execuções')
plt.ylim(0, 10000)
plt.show()
"""


#print('Lista aleatoria: ', A)
#print('Maior valor da lista: ', max(A))
#print('Ordenado pelo Bubblesort puro: ', bubble(A))
# bubble(A)
# bubble_v2(A)
#print('Ordenado pelo Bubblesort otimizado: ', bubble_v2(A))
