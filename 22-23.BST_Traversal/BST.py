class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        left = ' ' if self.left is None else f'({self.left.value})<-'

        right = ' ' if self.right is None else f'->({self.right.value})'

        return f'{left} ({self.value}) {right}'

    def __repr__(self):
        return str(self.value)


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

    def BFS(self):
        """ Breadth first search """
        queue = []
        visited = []
        node = self.root

        queue.append(node)

        while (len(queue) > 0):
            node = queue.pop(0)
            visited.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return visited

    def DFS_pre_order(self):
        """ Depth first search - pre order """
        visited = []

        def traverse(node):
            visited.append(node.value)

            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(self.root)

        return visited

    def DFS_post_order(self):
        """ Depth first search - post order """
        visited = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

            visited.append(node.value)

        traverse(self.root)

        return visited

    def DFS_in_order(self):
        """ Depth first search - in order """
        visited = []

        def traverse(node):
            if node.left:
                traverse(node.left)

            visited.append(node.value)

            if node.right:
                traverse(node.right)

        traverse(self.root)

        return visited


bst = BinarySearchTree()
bst.insert(10)
bst.insert(10)
bst.insert(8)
bst.insert(16)
bst.insert(7)
bst.insert(88)
bst.insert(11)
bst.insert(100)
bst.insert(33)
#       10
#    8      16
# 7      11      88
#             33      100
print(bst.root)
print(bst.find(8))
print(bst.find(9))
print(bst.BFS())
# [10, 8, 16, 7, 11, 88, 33, 100]
print(bst.DFS_pre_order())
# [10, 8, 7, 16, 11, 88, 33, 100]
print(bst.DFS_post_order())
# [7, 8, 11, 33, 100, 88, 16, 10]
print(bst.DFS_in_order())
# [7, 8, 10, 11, 16, 33, 88, 100]
