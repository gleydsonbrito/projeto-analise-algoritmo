import random as rnd


def bubbleSort5(A, d=1):
    # Para melhorar o desempenho do bubblesort5
    # podemos implementar a técnica de não verificar
    # a parte já ordenada da lista
    # com isso inclui uma variável parteOrdenada
    # que vai crescendo a cada iteração do while e
    # desconsiderando a parte que já está ordenada pois a lista
    # só vai até n - parteOrdenada
    n = len(A) - 1
    s = 0
    c = " "
    ordenado = False
    parteOrdenada = 0
    while not ordenado:
        ordenado = True
        for i in range(n-parteOrdenada):
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
        # melhoria do algoritmo
        parteOrdenada = parteOrdenada+1
    print(s, " passos")


print("Caso aleatório")
w = rnd.sample(range(10, 100), 15)
print(w)
s = w.copy()
print('Sort-5')
bubbleSort5(s)
print(w)

print("\nPior caso")
w = list(range(150, 0, -10))
print(w)
s = w.copy()
print('Sort-5')
bubbleSort5(s)

print("\nMelhor caso")
w = list(range(10, 160, 10))
print(w)
s = w.copy()
print('Sort-5')
bubbleSort5(s)
