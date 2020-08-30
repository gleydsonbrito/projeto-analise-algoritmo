TEXT_TO_ENCODE = "ABBACADCA"
print("Texto para codificar: ", TEXT_TO_ENCODE)


class Node:
    def __init__(self, key, frequency, left=None, right=None):
        self.key = key
        self.frequency = frequency
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.key)+"="+str(self.frequency)

    def Print_Tree(self):
        if self.left is not None:
            self.left.Print_Tree()
            print("0")
        print(self.key, end=' - ')
        if self.right is not None:
            self.right.Print_Tree()


listOfNodeCharacters = []


def createListOfNodes(TEXT):
    for char in TEXT:
        node = Node(char, 1)
        listOfNodeCharacters.append(node)


createListOfNodes(TEXT_TO_ENCODE)

print("Lista de caracteres: ", listOfNodeCharacters)

frequencyList = []


def countFequency(CHARACTERS_LIST):
    if len(frequencyList) == 0:
        frequencyList.append(CHARACTERS_LIST[0])
        return countFequency(CHARACTERS_LIST)

    for i in range(1, len(CHARACTERS_LIST)):
        index = exist(CHARACTERS_LIST[i].key, frequencyList)
        if index >= 0:
            frequencyList[index].frequency = frequencyList[index].frequency + 1
        else:
            frequencyList.append(CHARACTERS_LIST[i])


def exist(KEY, LIST):
    for i in range(0, len(LIST)):
        if KEY == LIST[i].key:
            return i
    return -1


countFequency(listOfNodeCharacters)


def sortListByFrequencyPriority(LIST):
    n = len(LIST)
    for j in range(0, n-1):
        for i in range(0, n-1):
            if LIST[i].frequency < LIST[i + 1].frequency:
                aux = LIST[i]
                LIST[i] = LIST[i+1]
                LIST[i + 1] = aux
    return LIST


frequencyList = sortListByFrequencyPriority(frequencyList)
print("Lista de frequência: ", frequencyList)


def createTree(LIST):
    while len(LIST) > 1:
        childLeft = LIST[-1]
        childRight = LIST[-2]

        LIST = LIST[:-2]

        P = Node(1, childLeft.frequency +
                 childRight.frequency, childLeft, childRight)

        LIST.append(P)
        LIST = sortListByFrequencyPriority(LIST)
    return LIST


frequencyList = createTree(frequencyList)

frequencyList[0].Print_Tree()
