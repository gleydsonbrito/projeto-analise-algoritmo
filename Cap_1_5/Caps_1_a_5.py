import math

lista_em_ordem = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_fora_de_ordem = [3, 5, 1, 4, 2, 6, 7, 8, 0, 9]

# Algoritmo 1.1 BuscaLinar(A, n, k)


def BuscaLinear(A, k, n=None):
    i = 1
    n = len(A) - 1

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
print('Busca LinearEmOrdem3.3 Resultado Esperado qundo x está na lista: 4')
print('Busca LinearEmOrdem3.3 Resultado Obtido: ',
      BuscaLinearEmOrdem33(lista_em_ordem, 5))
print('Busca LinearEmOrdem3.3 Resultado Esperado quando x NÃO está na lista: -1')
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


# BuscaLinar(A, n, k) versão mais recente do livro.
# Feito por engano


def BuscaLinearII(A, k, n=None):
    i = 1
    n = len(A) - 1

    while i <= n:
        if A[i] == k:
            return i
        i = i + 1
    return -1


# saída
print('BuscaLinear5.1 Resultado Esperado quando k está na lista: 7')
print('BuscaLinear5.1 Resultado Obtido: ',
      BuscaLinearII(lista_fora_de_ordem, 8))
print('BuscaLinear5.1 Resultado Esperado quando k NÃO está na lista: -1')
print('BuscaLinear5.1 Resultado Obtido: ',
      BuscaLinearII(lista_fora_de_ordem, 12))


# Algoritmo 5.2 SomaK(A, k, n)

def SomaK(A, k, n=None):
    n = len(A)
    for j in range(0, n):
        i = BuscaLinearII(A, k - A[j], n)
        if i != -1 and i != j:
            return [i, j]

    return [-1, -1]


# saída
print('SomaK Resultado Esperado: [1, 0]')
print('SomaK Resultado Obtido: ', SomaK(lista_fora_de_ordem, 8))


# Algoritmo 5.3 SomaK_V2(A, k, n)

def SomaK_V2(A, k, n=None):
    n = len(A)
    for i in range(0, n):
        j = i + 1
        for j in range(0, n):
            if A[i] + A[j] == k:
                return [i, j]

    return [-1, -1]


# saída
print('SomaK_V2 Resultado Esperado: [1, 0]')
print('SomaK_V2 Resultado Obtido: ', SomaK(lista_fora_de_ordem, 8))


# Algoritmo 5.1 BuscaLinearRecursiva(A, x, n)

def BuscaLinearRecursiva(A, x, n=None):
    if n is None:
        n = len(A)-1
    if n == 0:
        return -1
    if A[n] == x:
        return n
    return BuscaLinearRecursiva(A, x, n-1)


# saída
print('BuscaLinearRecursiva Resultado Esperado: 3')
print('BuscaLinearRecursiva Resultado Obtido: ',
      BuscaLinearRecursiva(lista_fora_de_ordem, 4))

# Algoritmo 5.2 Fatorial(n)


def Fatorial(n):
    if n == 0:
        return 1
    return n*Fatorial(n-1)


# Algortimo 5.3 Potencia(x, n)


def PotenciaV1(x, n):
    if n == 0:
        return 1
    return x*PotenciaV1(x, n-1)


# saída
print('PotenciaV1 Resultado Esperado: 81')
print('PotenciaV1 Resultado Obtido: ', PotenciaV1(9, 2))

# Algoritmo 5.4 PotenciaV2(x, n)


def PotenciaV2(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return PotenciaV2(x, n/2)*PotenciaV2(x, n/2)
    else:
        return x*PotenciaV1(x, (n-1)/2)*PotenciaV2(x, (n-1)/2)


# saída
print('PotenciaV2 Resultado Esperado: 64')
print('PotenciaV2 Resultado Obtido: ', PotenciaV2(8, 2))


# Algoritmo 5.5 PotenciaV3(x, n)

def PotenciaV3(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        aux = PotenciaV2(x, n/2)
        return aux * aux
    else:
        aux = PotenciaV1(x, (n-1)/2)
        return x * aux * aux


# saída
print('PotenciaV3 Resultado Esperado: 49 ')
print('PotenciaV3 Resultado Obtido: ', PotenciaV3(7, 2))


# Algoritmo 5.6 BuscaBinariaRecursiva(A, esq, dir, x)

def BuscaBinariaRecursiva(A, x, esq=0, di=None):
    if di is None:
        di = len(A)-1

    meio = (esq+di)//2

    if A[meio] == x:
        return meio
    elif x < A[meio]:
        BuscaBinariaRecursiva(A, x, esq, meio-1)
    else:
        BuscaBinariaRecursiva(A, x, meio + 1, di)


# saída
print('BuscaBinariaRecursiva Resultado Esperado:  ')
print('BuscaBinariaRecursiva Resultado Obtido: ',
      BuscaBinariaRecursiva(lista_em_ordem, 7))
