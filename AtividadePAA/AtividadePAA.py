#INÍCIO DA IMPLEMENTAÇÃO DA FILA EM LISTA ENCADEADA SIMPLES;

#Define os objetos 'nós' da Fila
class Node: 
    def __init__(self, data):
        self.data = data #armazena os dados do objeto;
        self.next = None  #define a referência para o próximo objeto, esse atributo é null quando o objeto é a cauda da fila;

    def __repr__(self):
        return self.data

# -ATENDE AO ITEM 3 DA LISTA DE EXERCÍCIOS;
#"3. Implementar uma Fila em uma lista simplesmente encadeada";
#A classe QueueLinkedList implementa uma Fila em uma lista encadeada simples;
#Possui um atruibuto cabeça que aponta pra null quando a Fila está vazia;
class QueueLinkedList: 
    def __init__(self): #Método construtor que inicia uma Fila vazia;
        self.head = None
    
    #representação da Fila, foi adaptada do Link passado na aula;
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data+'->{ '+str(node.next)+' }')
            node = node.next
        return " / ".join(nodes)

   #Método que adiciona objetos no final da Fila 
    def add(self, data):
      if self.head is None:
        self.head = Node(data)
      else:
        current = self.head

        while current.next is not None: #procura o último elemento
          current = current.next

        current.next = Node(data)

    #recupera o elemento mais antigo elemnento a entrar na Fila (LIFO)
    def get(self):
      if self.head is None: #checa se a lista está vazia
        return 'Empty List'
      else:
        current = self.head
        self.head = self.head.next
        return current
    
    # -ATENDE AO ITEM 1 DA LISTA DE EXERCÍCIOS;
    #"1. Implemente o algoritmo de remoção em listas simplesmente encadeadas."
    def remove(self, key):
      if self.head is None: 
        return 'Empty List'

      elif self.head.data == key:
            self.head = self.head.next
            return key

      current = self.head

      while (current is not None):
        if current.next is not None and current.next.data == key:
          current.next = current.next.next
          return key;
        else:
          current = current.next

      return 'Your key does not exist'


#Instancia uma Fila vazia;
queue = QueueLinkedList();

#print(queue)

#Adicionando elementos;
queue.add('a')
queue.add('b')
queue.add('c')
queue.add('d')

#imprime a lista após as inserções
#print(queue)
#SAÍDA: a->{ b } / b->{ c } / c->{ d } / d->{ None }

#removendo o elemento 'b'
#print(queue.remove('b')) #retorna o elemento removido, isso pode mudar dependendo dos requisitos da implementação
#SAÍDA: b

#Impressão da lista após a remoção;
#print(queue)
#SAÍDA: a->{ c } / c->{ d } / d->{ None }
#o objeto 'b' não existe e 'a' agora aponta para 'c';

#Recuperando o elemento mais antido da Fila
#print(queue.get())
#SAÍDA: a

#Impressão da fila após desenfileirar;
#print(queue)
#SAÍDA: b->{ c } / c->{ d } / d->{ None }
#FIM DA IMPLEMENTAÇÃO DA FILA EM LISTA ENCADEADA SIMPLES;



#INÍCIO DA IMPLEMENTAÇÃO DA ÁRVORE BINÁRIA DE BUSCA E SUAS OPERAÇÕES;
#IMPLEMENTANDO AS OPERAÇÕES DA PÁG. 99 DO LIVRO DE CARLA NEGRI
#ATENDE AOS ITENS 04 4 05  
class Node:
    #definição de um objeto nó da árvore binária de busca
    def __init__(self, data):
        self.data = data #carrega os dados
        self.left = None #apota para o nó a esquerda
        self.right = None #aponta para o nó a direita

    #função para imprimir a árvore
    #adaptado do link : https://tinyurl.com/yxco7zc7
    def Print_Tree(self):
        if self.left is not None:
            self.left.Print_Tree()
        print(self.data, end=' - ') 
        if self.right is not None:
            self.right.Print_Tree()
    
    #Método implementa a inserção em uma árvore binária
    def put(self, key):
        if self.data is not None: #checa se a raíz da árvore é nula
            if key < self.data: #checa se o a chave para ser inserida é < que a chave da raíz
                if self.left is None: #se for menor e nula, cria um novo a partir do ramo esquerdo da raiz
                    self.left = Node(key)
                else:
                    self.left.put(key) #se não for nula faz uma inserção recursiva a partir desta raiz
            elif key > self.data: #mesmo processo acima, para criar um nói a partir do ramo direito
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.put(key)
        else:
            self.data = Node(key)
    
    #Método implementa a busca em uma árvore binária
    def find(self, key):
        #checa se a árvore está vazia ou a chave está na raiz
        if self.data is None or self.data == key: return self.data
        
        #checa se a chave é < que o elemento buscado
        if key < self.data:
            if self.left is None: #Se o nó é nulo, retorna -1
                return -1
            else:
                return self.left.find(key) #Se o nó é não nulo, faz uma busca recursiva a partir deste nó
        elif key > self.data:
            if self.right is None:
                return -1
            else:
                return self.right.find(key) #Busca recursiva a partir do nó à direita
        else:
            return -1
    #Atende ao item 5: Implementar as operações da página 99
    #obtém o nõ mínimo a partir de determinado nó
    def minimum(self):
        if self.left:
            return self.left.minimum()
        return self.data
    
    #obtém o nõ máximo a partir de determinado nó
    def maximum(self):
        if self.right:
            return self.right.maximum()
        return self.data
    #obtém Sucessor a partir de determinado nó
    def sucessor(self):
        return self.minimum()
    #obtém Predecessor a partir de determinado nó
    def predecessor(self):
        return self.maximum()
    
   #Método implementa a remoção em uma árvore binária
    def remove(self, key):
        #Checa se a árvore está vazia ou se a chave buscada está na raiz
        if self.data == key or self.data is None:
            ret = self.data
            self.data = None
            return ret
        
        if key < self.data:
            if self.left is not None:
                return self.left.remove(key)#Faz uma busca recursiva à esquerda
        elif key > self.data:
            if self.right is not None:
                return self.right. remove(key)#Faz uma busca recursiva à direita
        else:
            #se o nó só possui filho direito, o nó a ser excluído recebbe a subárvore à direita
            if self.left is None:
                self.data = self.right
                self.right = None
            #se o nó só possui filho esquerdo, o nó a ser excluído recebbe a subárvore à esquerda
            elif self.right is None:
                self.data = self.left
                self.left = Node
            else:
            #Se o nó possui filhos a esquerda e direita
            #o nó a ser excluído recebe seu sucessor e seu sucessor e removidso da posição 
            #em que se encontrava
                self.data = self.right.minimum()
                self.right.minimum().remove(key)

        return self.data  


    
#cria o nó raiz
node = Node("100")

#insere dados na árvore
node.put("90")
node.put("110")
node.put("70")
node.put("95")

#imprime a árvore depois das inserções
node.Print_Tree()
#SAÍDA: 100 110 70 90 95

#Realizando buscas na árvore binária
#print(node.find("100"))
#SAÍDA: 100 -> retorna o valor da raiz buscada

#print(node.find("90"))
#SAÍDA: 90 -> retorna o valor da raiz buscada

#print(node.find("70"))
#SAÍDA: 70 -> retorna o valor da raiz buscada

#testando a busca para um elemento que não pertence  a árvore
#print(node.find("x"))
#SAÍDA: -1

#Testando a remoção de um elemento da árvore;
#node.remove("70")
#SAÍDA: 100 - 110 - None - 90 - 95 - 

#print()
#node.Print_Tree()

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



