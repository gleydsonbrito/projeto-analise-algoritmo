class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def Print_Tree(self):
        if self.left is not None:
            self.left.Print_Tree()
        print(self.data, end=' - ')
        if self.right is not None:
            self.right.Print_Tree()

    def insert(self, key):
        if self.data is None:
            self.data = Node(key)

        if key < self.data:
            if self.left is None:
                self.left = Node(key)
            else:
                return self.left.insert(key)
        elif key > self.data:
            if self.right is None:
                self.right = Node(key)
            else:
                return self.right.insert(key)

    def find(self, key):
        if self.data is None: return "Empty Tree"

        if self.data == key:
            return self.data
        else:
            if key < self.data:
                if self.left is None:
                    return -1
                elif self.left == key:
                    return self.left
                else:
                    return self.left.find(key)
            else:
                if self.right is None:
                    return -1
                elif self.right == key:
                    return self.left
                else:
                    return self.right.find(key)

    def minimum(self):
        if self.left is not None:
            return self.left.minimum()
        return self.data

    def maximum(self):
        if self.right is not None:
            return self.right.maximum()
        return self.data

    def sucessor(self):
        return self.minimum()

    def predecessor(self):
        return self.maximum()

    def remove(self, key):
        if self.data is None: return self.data

        if key < self.data:
            if self.left is not None:
                return self.left.remove(key)
            else:
                return 'key not found'
        elif key > self.data:
            if self.right is not None:
                return self.right.remove(key)
            else:
                return 'key not found'
        else:
            if self.left is None:
                self.data = self.right
            elif self.right is None:
                self.data = self.left
            else:
                self.data = self.right.minimum()
                return self.right.remove(key)


node = Node('100')

node.insert('90')
node.insert('110')
node.insert('150')
node.insert('130')
node.insert('70')
node.insert('120')
node.insert('85')
node.insert('95')

node.Print_Tree()

node.remove("130")
print("-")
node.Print_Tree()



