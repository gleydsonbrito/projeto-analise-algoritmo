test = [9,7,6,5,4,3,2,1,0]

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

printA(test)

bubbleSort(test)
print()

printA(test)