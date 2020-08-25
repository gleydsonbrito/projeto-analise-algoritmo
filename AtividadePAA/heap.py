#INÍCIO HEAP E SUAS OPERAÇÕES

#ATENDE AO ITEM 06 IMPLEMENTAR HEAP E SUAS OPERAÇÕES
#Liste de prioridade(exemplo)
PRIORITY_LIST = [30, 27, 24, 20, 25, 19, 22, 10, 15, 40, 18, 14, 11, 17, 21, 8, 1, 3, 4, 9, 7, 6]
#30 -> 12
#15 -> 45
#Vetor que será utilizado para armazenar os elementos da fila de prioridades
H = []

#Vetor utilizar na Construção do Heap
BUILD_HEAP = [4, 7, 3, 10, 2, 15, 1, 9, 6, 23, 42, 34, 65,  20]
BH = []
#Classe que que cria um elemento da Heap
#Possui 2 atrubutos: prioridade e indice, cada objeto desse será adicionando ao vetor H
class HeapElements:
    def __init__(self, priority, index):
        self.priority = priority
        self.index = index
    #Define como esse objeto será impresso
    def __repr__(self):
        return "[prior: "+str(self.priority)+" -> index: "+str(self.index)+"]"


#Método para imprimir a lista de prioridades, vetor H
def printH(text, H):
    print(text)
    for i in H:
        print(i)

#Método CORRIGE DESCENDO. 
def rectifyDown(H, i):
    #Pega a posição que foi modificada e de onde a correção iniciará
    greater = i
    #Avalia se o filho esquerdo da posição [i] ([2i]) é menor que a última posição do array
    #Avalia se a prioridade do Filho é maior que a do Pai
    if (2*i <= len(H)) and (H[(2*i)].priority > H[greater].priority):
        greater = 2*i
    
    #Igual a avaliação anterior, só que para o filho direito
    if ((2*i) + 1 <= len(H)) and (H[(2*i) + 1].priority > H[greater].priority):
        greater = (2*i) + 1
    
    #Caso a posição do elemento de maior prioridade seja diferente da posição da entreda da função
    #SIgnofica que um dos filhos tem prioridade maior que a do seu pai
    #Então esses elementos precisam trocar de lugar para manter a condição de Heap
    if greater != i:
        #armazena temporariamente o objeto que será trocado 
        temporary = H[i].priority
        #troca a posição do pai com seu filho de maior prioridade
        H[i].priority = H[greater].priority
        H[greater].priority = temporary

        #Faz uma chamada recursiva a partir da nova posição para continuar corrigindo o Heap
        return rectifyDown(H, greater)

#Método CORRIGE SUBINDO. 
def rectifyUp(H, i):
    #pega o elemnto Pai do elemento que será corrigido
    parent = int(i/2)

    #Avalia quem tem maior prioridade e faz a troca
    if i >= 1 and H[i].priority > H[parent].priority:
        temporary = H[i].priority
        H[i].priority = H[parent].priority
        H[parent].priority = temporary

        #faz uma chamada recursvia para o próxim Pai e segue corrigindo até que chegue na "raiz"
        return rectifyUp(H, parent)

#Funão que constroi um heap a patir de qualquer vetor 
def buildHeap(build_heap):
    #pega o primeiro elemento que possui filhos e aplica o algoritmo de corrigir desecendo
    leng = int((len(build_heap)/2)-1)
    while leng >= 0:
        #a partir do primeiro elemento que possui filhos
        #aplica o corrige descendo até o início do vetor 
        rectifyDown(BH, leng)
        #decrementa até chegar na posição 0 do vetor 
        leng = leng -1

#Função insere elementos em um heap
def insert(H, value):
    #pega o tamanho do vetor para se o índice do novo elemento
    tam = len(H)
    #adiciona o elemento no final, primeira posição disponível
    H.append(HeapElements(value, tam))
    #a partir a últim a posição corrige o vetor subindo até a raiz
    return rectifyUp(H, tam)


#Função para remover um elemento do heap
def remove(H):
    #cria o elemento que vai ser retornado
    x = None
    leng = len(H)
    #faz a troca do primeir com o último elemento
    #no final corrige o vetor descendo
    if leng >= 1:
        x = H[0]
        H[0] = H[leng -1]
        H[0].index = 0
        H.pop(leng-1)
        rectifyUp(H, 0)
    #retorno o elemento removido
    return x
#Função que altera a prioridade de um elemento na heap
def changeHeap(H, i, k):
    aux = H[i].priority
    #seta a nova prioridade no elemento H[i] 
    H[i].priority = k

    #se a prioridade anterior do elemento for menor, corrige subindo
    if aux < k: return rectifyUp(H, i)

      #se a prioridade anterior do elemento for maior, corrige descendo
    if aux > k: return rectifyDown(H, i)

#Simples função para criar uma fila de prioridades com o vetor de prioridade e os objetos da classe HeapElements
def createPriorityQueue(queue, vector):
    index = 0
    for priority in queue:
        element = HeapElements(priority, index)
        vector.append(element)
        index=index+1

createPriorityQueue(PRIORITY_LIST, H)

createPriorityQueue(BUILD_HEAP, BH)

#Imprime a fila de prioridades
printH("Lista Inicial", H)


#Corrige descendo a fila de porioridades com a alteração do elemento
#na posição 0. Era 30 na H[0], foi substituido pra 12.
#Agora a posição H[0] = 12
#rectifyDown(H, 0)

#Imprime a fila corrigida.
#O elemento 12 agora está na posição H[9]
print("__________________")
#printH("Corrige Descendo", H)

#Corrige subindo a fila de porioridades com a alteração do elemento
#O elemento 45 foi adicionando na posição 8
#Após a correção subndo o elemnento 45 vai para sua posição corre H[0]
#rectifyUp(H, 8)

#Imprime lista após a correção
#printH("Corrige Descendo", H)

#Lista que será convertida em heap
#printH("Lista para construir o Heap", BH)

#Função que transforma o vetor em Heap
#buildHeap(BH)
#Lista após a transformação em heap
#printH("Construindo Heap", BH)

#Inserindo um elemento novo no heap
#insert(H, 79);

#Imprimindo a heap após a inserção, 
#o elemento novo, 79, foi para a pósição H[0], posição com maior prioridade
#printH("Inserindo elemento no Heap", H)

#Remove o elemento de maior prioridade
#print(remove(H))

#printH("Removendo um elemento do heap", H)

#Alterando a prioridade do elemento na posição H[0] de 30 para 2
#changeHeap(H, 0, 2)
#Imprimindo a lista após a alteração
#printH("Alterando um elemento da Heap", H)

#FIM HEAP E SUAS OPERAÇÕES