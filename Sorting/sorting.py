bubble_test = [9,7,6,5,4,3,2,1,0]
#INÍCIO BUBBLESORT
def bubbleSort(array):
    n = len(array)
    for j in range(n - 1):
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                aux = array[i]
                array[i] = array[i+1]
                array[i + 1] = aux
    return array

def printA(array):
    for i in array:
        print(i, end=' ')

#printA(bubble_test)

#bubbleSort(bubble_test)
#print("BubbleSort", "**************")
#printA(bubble_test)
#FIM BUBBLESORT

arrayTest = [46, 68, 3, 40, 59, 20, 88, 12, 6, 86, 57, 47, 71, 92, 81, 95, 11, 4, 52, 35, 51]



#INÍCIO INSERTIONSORT
def insertionSort(A, n=None):
    n = len(A) - 1
    for i in range(n):
        if i == 0: continue
        current = A[i]
        j = i - 1
        while j >= 0 and A[j] > current:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = current
    return A


print(arrayTest)
print("***************")
# print("InsertionSort", insertionSort(arrayTest))
#FIM INSERTIONSORT

#INÍCIO MERGESORT
# função auxiliar do mergesort
def merge(A, start, midle, end):
    left = A[start:midle]  # cria duas listas para armazenar o vetores dividos
    right = A[midle:end]

    left_top, right_top = 0, 0  # cria var aux para controlar o topo das listas acima

    for k in range(start, end):
        if left_top >= len(left):  # verifica se a lista esquerda já foi esgotada
            # se a lista esquerda foi esgotada, pega o valor da pilha direita
            A[k] = right[right_top]
            right_top = right_top + 1
        # verifica se a lista da direita já foi esgotada
        elif right_top >= len(right):
            # se a lista esquerda foi esgotada, pega o valor da pilha esquerda
            A[k] = left[left_top]
            left_top = left_top + 1
        # verifica o valor no topo de cada pilha
        elif left[left_top] < right[right_top]:  # valor do topo da pilha esqueda é menor
            A[k] = left[left_top]  # pega o valor da pilha esquerda
            # incrementa a pilha, pra não avaliar o mesmo valor na próxima iteração
            left_top = left_top + 1
        else:
            A[k] = right[right_top]  # Se o valor da pilha direita é menor
            right_top = right_top + 1  # pega o topo do pilha dirieita

# implementação do Shellsort
def mergeSort(A, start=0, end=None):
    if end is None:  # atribui o valor do final da lista A
        end = len(A)

    if (end - start) > 1:  # checa se a diferença entre a posição final e a inicial é > que 1
        # quando essa diferença é maior que 1, a lista ainda tem mais de dois elementos
        # e precisa ser dividida
        midle = (start + end)//2  # pega o valor inteiro do meio da lista
        # faz uma chamada recursiva para dividir o subvetor inicial
        mergeSort(A, start, midle)
        # faz uma chamada  recursiva para dividir o subvetor final
        mergeSort(A, midle, end)
        # chama a funçã auxilia para ordenar recursivamente os subvetore e combiuná-los
        merge(A, start, midle, end)

#mergeSort(arrayTest)
#print("MergeSort", arrayTest)
#FIM MERGESORT

#INÍCIO SELECTIONSORT
#implementa a ordenação por seleção
#recebe uma lista como entrada e devolve a referida lista ordenada em ordem não decrescente
def selectionSort(A):
    #pega o tamanho da lita
    i = len(A) - 1
    #percorre o lista do final para o inicío
    while i >=  1:
        #pega o último valor da lista como ídice para o maior valor da lista
        maxIndex = i
        #percorre a lista desde o início para descobrir o maior valor da lista
        for j in range(0, i):
            #se um valor em determinada posição for maior que o valor do maior índice
            #a variável maior indice recebe esse valor
            if A[j] > A[maxIndex]:
                maxIndex = j

        #ao final do FOR, troca o valor do maior índice com a última posição da lista
        #e decrementa a lista em uma posição, e refaz todo o processo para esse sub vetor
        #que vai agora de n-1 até 0
        aux = A[maxIndex]
        A[maxIndex] = A[i]
        A[i] = aux
        i = i - 1
    #retorna lista ordenada
    return A

#immprime a lista ordenada
#print("SelectionSort", selectionSort(arrayTest))
#FIM SELECTIONSORT

#INÍCIO HEAPSORT
#função que implementa o corrige descendo
def heapsort(H, i):
    greater = i
    if 2*i < len(H) and H[2*i] > H[greater]:
        greater = 2*i
    if 2*i+1 < len(H) and H[2*i+1] > H[greater]:
        greater = (2*i)+1

    if greater != i:
        aux = H[i]
        H[i] = H[greater]
        H[greater] = aux
        heapsort(H, greater)

#função que constroi um heap binário a partir de qualquer lista
def heapsortBuild(H):
    i = (len(H)//2)-1
    for i in range(i, -1, -1):
        heapsort(H, i)
    return H

#função que ordena a paritr de um heap binário   
def heapsortAlg(A):
    #inicia transformando a lista em um heap binário
    i = len(A)-1
    #percorre a lista em ordem decrescente
    for i in range(i, 1, -1):
        #troca o primeiro elemento da lista, o maior valor de um heap binário
        aux = A[0]
        A[0] = A[i]
        A[i] = aux
        A[-1]  
        #corrige o heap descendo
        heapsort(A, 0)

#H = heapsortBuild(arrayTest)
#heapsortAlg(H)
#print(arrayTest)

#INÍCIO QUICKSORT
#define o algoritmo de ordenação quicksort
#recebe uma lista, parâmetro de inicio=0 e fim
def quicksort(A, start=0, end=None):
    #define o fim a partir da ultima posição da lista -1
    if end is None: end = len(A)-1

    #checa se a lista tem mais de um elemento
    if start < end:
        #devolve a posição final do pivot após particionar o vetor
        part = partition(A, start, end)
        #realiza uma chamada recursiva a partição esquerda
        quicksort(A, start, part-1)
        #realiza uma chamada recursiva a direita
        quicksort(A, part+1, end)
#define a posição das partições
def partition(A, start, end):
    #define o pivot como o último elemento da lista
    pivot = A[end]
    #define a posição da partição que vai estar a direita do pivot
    right_line_pivot = start
    #pecore o vetor a partir do inicio, tendo como base os numeros que devem ficar a esquerad do pivot
    #a lista vai da posição 0 até a posição pivot-1, já que o pivot foi definido como último elemnento da lista
    #left_line_pivot define a partição de conterá os elementos a esquerda do pivot
    for left_line_pivot in range(start, end):
        #caso o valor da lista seja menor que o pivot
        if A[left_line_pivot] <= pivot:
            #invertemos os valores para as posições adequadas
            A[left_line_pivot], A[right_line_pivot] = A[right_line_pivot], A[left_line_pivot]
            #avançamos o índex que delimita os elementos que devem ficar a direita do pivot
            right_line_pivot = right_line_pivot + 1
    #por fim trocamos o valor que marca os elementos que devem estar a direita do pivot com o pivot
    #assim, teremos a esquerad do pivot todos os elementos que são menores que ele
    # e a direita todos os elementos que são maiores que o pivot
    A[right_line_pivot], A[end] = A[end], A[right_line_pivot]
    #retorna a posição do pivot, a partir da qual as novas partições devem ser analisadas
    return right_line_pivot

#quicksort(arrayTest)
#print(arrayTest)
#FIM QUICKSORT

#INÍCIO COUNTSORT
A = [3, 0, 5, 4, 3, 0, 1, 2]

def countsort(A, k=0):
    B = []
    C = []
    #inicializa um vetor B com o valor 0 para todos os elementos
    for b in range(0, len(A)):
        B.append(0)

    #pega o maior valor do array A para ser o tamaho k da lista
    for n in range(0, len(A)):
        if A[n] > k:
            k = A[n]
    
    #atribui 0 a todas as posições do vetor C
    for i in range(0, k+1):
        C.append(0)
    
    #conta as ocorrencias do valor A[i] no vetor C[A[i]]
    #dessa forma, as quantidades dos valores de A serão acumuladas nas respectivas
    #posições do vetor C[0..k]
    for j in range(0, len(A)):
        C[A[j]] = C[A[j]]+1

    #acumula as ocorrências de A em C
    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]
    
    j = len(A)-1
    #ordena o vetor B a partir dos valores de 
    while j >= 0:
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]] - 1
        j=j-1
    return B

print(countsort(A))

#FIM COUNTSORT