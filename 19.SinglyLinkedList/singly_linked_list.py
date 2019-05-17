class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f'Node: value={self.value}'


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(current.value)
            current = current.next
        return str(result)

    def push(self, value):
        """
        Add a node with value of {value} at the tail of the list.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def pop(self):
        """
        Delete the node at the tail and returns the deleted node.
        """
        if self.tail is None:
            return None

        current = self.head
        new_tail = current

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return current

        while current.next:
            new_tail = current
            current = current.next

        new_tail.next = None
        self.tail = new_tail
        self.length -= 1

        return current

    def shift(self):
        """
        Delete the head node and returns it.
        """
        if self.length == 0:
            return None
        if self.length == 1:
            self.tail = None

        old_head = self.head
        self.head = old_head.next
        self.length -= 1

        return old_head

    def unshift(self, value):
        """
        Add a node with value of {value} at the head of the list.
        """
        new_head = Node(value)
        old_head = self.head

        if old_head is None:
            self.tail = new_head
        else:
            new_head.next = old_head
        self.head = new_head
        self.length += 1

    def get(self, idx):
        """
        Get the node at index of {idx}
        """
        if idx < 0 or idx >= self.length:
            return None

        current = self.head
        count = 0

        while count < idx:
            current = current.next
            count += 1

        return current

    def set(self, idx, value):
        """
        Set the value at index of {idx} to have a value of {value}. Returns True is the operation is successful.
        """
        found_node = self.get(idx)
        if found_node is None:
            return False

        found_node.value = value
        return True

    def insert(self, idx, value):
        """
        Insert a new node with value of {value} at the index of {idx}.
        """
        if idx < 0 or idx > self.length:
            return False

        if idx == 0:
            self.unshift(value)
            return True

        if idx == self.length:
            self.push(value)
            return True

        new_node = Node(value)
        previous = self.get(idx-1)
        current = previous.next

        previous.next = new_node
        new_node.next = current

        self.length += 1
        return True

    def remove(self, idx):
        """
        Remove the node at index of {idx}.
        Returns the removed node.
        """
        if idx < 0 or idx >= self.length:
            return None

        if idx == 0:
            return self.shift()

        if idx == self.length-1:
            return self.pop()

        previous = self.get(idx - 1)
        node_to_remove = previous.next

        previous.next = node_to_remove.next
        self.length -= 1

        return node_to_remove

    def reverse(self):
        """ 
        Reverse the whole list.
        """
        if self.length > 1:
            previous = self.head
            current = previous.next
            next_node = current.next

            while next_node is not self.tail:
                current.next = previous
                previous = current
                current = next_node
                next_node = next_node.next

            current.next = previous
            next_node.next = current

            self.tail, self.head = self.head, self.tail
            self.tail.next = None


# Tests
sll = SinglyLinkedList()
sll.push(0)
sll.push(1)
sll.push(2)
sll.push(3)
sll.push(4)
print(sll)
print(sll.head)
print(sll.tail)
print(sll.pop())
print(sll)
print(sll.shift())
print(sll)
sll.unshift(5)
print(sll)
print(sll.get(3))
sll.set(3, 100)
print(sll)
sll.insert(1, 99)
print(sll)
sll.remove(3)
print(sll)
sll.reverse()
print(sll)
