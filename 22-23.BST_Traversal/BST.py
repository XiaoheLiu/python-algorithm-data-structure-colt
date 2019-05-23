class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        left = ' ' if self.left is None else f'({self.left.value})<-'

        right = ' ' if self.right is None else f'->({self.right.value})'

        return f'{left} ({self.value}) {right}'


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Insert value into BST.
        Returns the updated BST if successfully inserted,
        otherwise returns None.
        """
        node = Node(value)

        if self.root is None:
            self.root = node
            return self

        current = self.root
        while True:
            if value == current.value:
                return None
            if value < current.value:
                if current.left is None:
                    current.left = node
                    return self
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return self
                else:
                    current = current.right

    def find(self, value):
        if self.root is None:
            return None

        current = self.root
        found = False

        while current is not None and not found:
            if value == current.value:
                found = True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        if not found:
            return None

        return current


bst = BinarySearchTree()
bst.insert(10)
bst.insert(10)
bst.insert(8)
bst.insert(16)
print(bst.root)
print(bst.find(8))
print(bst.find(9))
