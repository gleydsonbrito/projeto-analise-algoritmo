import math

lista_em_ordem = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_fora_de_ordem = [3, 5, 1, 4, 2, 6, 7, 8, 0, 9]

# Algoritmo 1.1 BuscaLinar(A, n, k)


def BuscaLinear(A, k, n=None):
    i = 1
    n = len(A)

    while i <= n:
        if A[i] == k:
            return i
        i = i + 1


# saída
print('Busca Linear Resultado Esperado: 7')
print('Busca Linear Resultado Obtido: ', BuscaLinear(lista_fora_de_ordem, 8))


# Algoritmo 1.2 BuscaLinearEmOrdem(A, n, x)


def BuscaLinearEmOrdem(A, k, n=None):
    i = 1
    n = len(A)

    while i <= n and k >= A[i]:
        if A[i] == k:
            return i
        i = i + 1
    return -1


# saída
print('Busca LinearEmOrdem Resultado Esperado: 4')
print('Busca LinearEmOrdem Resultado Obtido: ',
      BuscaLinearEmOrdem(lista_em_ordem, 5))
print('Busca LinearEmOrdem Resultado Esperado: -1')
print('Busca LinearEmOrdem Resultado Obtido:',
      BuscaLinearEmOrdem(lista_em_ordem, 0))


# Algoritmo 1.3 BuscaBinária(A, k, n)

def BuscaBinária(A, k, n=None):
    n = len(A)

    esq = 1
    di = n - 1

    while esq <= di:
        meio = (di+esq)//2
        if A[meio] == k:
            return meio
        elif k > A[meio]:
            esq = meio + 1
        else:
            di = meio - 1
    return -1


# saída
print('Busca BuscaBinaria Resultado Esperado: 1')
print('Busca BuscaBinaria Resultado Obtido: ', BuscaBinária(lista_em_ordem, 2))
print('Busca BuscaBinaria Resultado Esperado: -1')
print('Busca BuscaBinaria Resultado Obtido: ',
      BuscaBinária(lista_em_ordem, 10))


# Algoritmo 2.1 Somatório(A, n)

def Somatório(A, n=None):
    n = len(A)
    soma = 0
    for i in range(0, n):
        soma = soma + A[i]
    return soma


# saída
print('Somatório de Resultado Esperado: 45')
print('Somatório Resultado Obtido: ', Somatório(lista_em_ordem))

# Algoritmo 2.2 Produtorio(A, n)


def Produtorio(A, n=None):
    n = len(A)
    prod = 1
    for i in range(0, n):
        prod = prod * A[i]
    return prod


# saída
print('Produtorio Resultado Esperado: 362880')
print('Produtorio Resultado Obtido: ', Produtorio(lista_em_ordem))

# Algoritmo 2.3 ConverteBase(n)


def ConverteBase(n=None):
    n = len(lista_em_ordem)
    B = [-1]*n
    i = 0
    t = n

    while t > 0:
        B[i] = t % 2
        i = i + 1
        t = t//2
    return B


# saída
print('ConverteBase Resultado Esperado: [1, 0, 0, 1, -1, -1, -1, -1, -1]')
print('ConverteBase Resultado Obtido: ', ConverteBase())

# Algoritmo 3.1 SomatorioPar(A, n)


def SomatorioPar(A, n=None):
    n = len(A)
    soma = 0

    for i in range(0, n):
        if A[i] % 2 == 0:
            soma = soma + A[i]
    return soma


# saída
print('SomatorioPar Resultado Esperado: 20')
print('SomatorioPar Resultado Obtido: ', SomatorioPar(lista_em_ordem))


# Algorimto 3.2 BuscaLinear(A, n, x)

def BuscaLinear32(A, x, n=None):
    n = len(A)
    i = 0
    while i <= n:
        if A[i] == x:
            return i
        i = i + 1
    return -1


# saída
print('Busca Linear32 Resultado Esperado: 7')
print('Busca Linear32 Resultado Obtido: ',
      BuscaLinear32(lista_fora_de_ordem, 8))


# Algorito 3.3 BuscaLinearEmOrdem(A, x, n)

def BuscaLinearEmOrdem33(A, x, n=None):
    n = len(A)
    i = 0

    while i <= n and x >= A[i]:
        if A[i] == x:
            return i
        i = i + 1
    return -1


# saída
print('Busca LinearEmOrdem3.3 Resultado Esperado está na lista: 4')
print('Busca LinearEmOrdem3.3 Resultado Obtido: ',
      BuscaLinearEmOrdem33(lista_em_ordem, 5))
print('Busca LinearEmOrdem3.3 Resultado Esperado não está na lista: -1')
print('Busca LinearEmOrdem3.3 Resultado Obtido:',
      BuscaLinearEmOrdem33(lista_em_ordem, 0))


# Algoritmo 3.4 BuscaBinaria(A, x, n)

def BuscaBinaria34(A, x, n=None):
    n = len(A)
    esq = 0
    di = n - 1
    while esq <= di:
        meio = (di+esq)//2
        if A[meio] == x:
            return meio
        elif x > A[meio]:
            esq = meio + 1
        else:
            di = meio - 1
    return -1


# saída
print('BuscaBinaria3.4 Resultado Esperado: 1')
print('BuscaBinaria3.4 Resultado Obtido: ',
      BuscaBinaria34(lista_em_ordem, 2))
print('BuscaBinaria3.4 Resultado Esperado: -1')
print('BuscaBinaria3.4 Resultado Obtido: ',
      BuscaBinaria34(lista_em_ordem, 10))
