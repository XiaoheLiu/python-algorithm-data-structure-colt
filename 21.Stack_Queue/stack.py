class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f'Node: value={self.value}'


class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)

        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.first, self.first.next = new_node, self.first

        self.size += 1

    def pop(self):
        if self.first is None:
            return None

        node = self.first

        if self.first is self.last:
            self.last = None
        self.first = node.next
        self.size -= 1

        return node.value


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
