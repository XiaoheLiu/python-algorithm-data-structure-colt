class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f'Node: value={self.value}'


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return str(result)

    def push(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            old_tail = self.tail
            old_tail.next = new_node
            new_node.prev = old_tail
            self.tail = new_node
        self.length += 1

        return self

    def pop(self):
        if self.length == 0:
            return None

        tail_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = tail_node.prev
            self.tail.next = None
            tail_node.pre = None
        self.length -= 1

        return tail_node

    def shift(self):
        """ Delete First """
        if self.length == 0:
            return None

        head_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = head_node.next
            self.head.prev = None
            head_node.next = None
        self.length -= 1

        return head_node

    def unshift(self, value):
        """ Add to first """
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self

    def get(self, idx):
        """ Efficient way to search a DLList """
        if idx < 0 or idx >= self.length:
            return None

        middle = self.length//2
        if idx <= middle:
            # Look up from the start if idx is small
            count = 0
            current = self.head
            while count < idx:
                current = current.next
                count += 1

        else:
            # Look up from the end if idx is large
            count = self.length - 1
            current = self.tail
            while count > idx:
                current = current.prev
                count -= 1

        return current

    def set(self, idx, value):
        node = self.get(idx)

        if node:
            node.value = value
            return True

        return False

    def insert(self, idx, value):
        if idx < 0 or idx > self.length:
            return False

        if idx == 0:
            self.unshift(value)
            return True

        if idx == self.length - 1:
            self.push(value)
            return True

        new_node = Node(value)
        before_node = self.get(idx - 1)
        after_node = before_node.next

        before_node.next = new_node
        new_node.prev = before_node
        new_node.next = after_node
        after_node.prev = new_node

        self.length += 1
        return True

    def remove(self, idx):
        if idx < 0 or idx >= self.length:
            return None

        if idx == 0:
            return self.shift()

        if idx == self.length - 1:
            return self.pop()

        node = self.get(idx)
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = None
        node.next = None

        self.length -= 1
        return node

    def reverse(self):
        if self.length <= 1:
            return self

        prev_node = self.head
        current = prev_node.next
        next_node = current.next

        while next_node is not self.tail:
            current.next = prev_node
            current.prev = next_node

            prev_node = current
            current = next_node
            next_node = next_node.next

        current.next = prev_node
        current.prev = next_node
        next_node.next = current

        self.head, self.tail = self.tail, self.head
        self.tail.next = None
        self.head.prev = None

        return self


        # Tests
dll = DoublyLinkedList()
dll.push(0)
dll.push(1)
dll.push(2)
dll.push(3)
print(dll)
print(dll.pop())
# print(dll.pop())
# print(dll.shift())
print(dll.shift())
print(dll.unshift(100))
print(dll.get(1))
dll.insert(0, 'Head')
dll.insert(3, 'Tail')
dll.insert(2, 'Middle')
dll.set(0, "UpdatedHead")
print(dll)
print(dll.remove(1))
dll.reverse()
print(dll)
