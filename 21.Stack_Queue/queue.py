class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f'Node: value={self.value}'


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, value):
        node = Node(value)

        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

        self.size += 1

    def dequeue(self):
        if self.first is None:
            return

        node = self.first
        if self.first is self.last:
            self.last = None

        self.first = self.first.next
        self.size -= 1

        return node.value


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
