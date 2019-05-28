class Node:
    def __init__(self, name: str, priority: int):
        self.name = name
        self.priority = priority  # small number means higher priority

    def __repr__(self):
        return f"{self.name}:🔥{self.priority}"


class PriorityQueue:
    """MinBinaryHeap"""

    def __init__(self):
        self.values = []

    def __str__(self):
        return str(self.values)

    def enqueue(self, name, priority):
        self.values.append(Node(name, priority))
        self.bubble_up()

    def bubble_up(self):
        idx = len(self.values) - 1
        parent_idx = (idx - 1) // 2  # parent index of idx

        # Bubbling up the new element to the correct place
        while idx > 0 and self.values[idx].priority < self.values[parent_idx].priority:
            # swap parent and child as long as child < parent
            self.values[idx], self.values[parent_idx] = self.values[parent_idx], self.values[idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2

        return self

    def dequeue(self):
        """
        Take out the root element (highest priority) and reorganize the heap to correct order.
        """
        min_task = self.values.pop(0)

        if len(self.values) > 0:
            end = self.values.pop()
            self.values.insert(0, end)
            self.sift_down()

        return min_task

    def sift_down(self):
        """
        Sink down the root element to the correct position
        (assuming heap is not empty.)
        """
        idx = 0

        while True:
            swap_idx = 0
            left = 2*idx + 1
            right = 2*idx + 2

            if left < len(self.values):
                if self.values[left].priority < self.values[idx].priority:
                    swap_idx = left

            if right < len(self.values):
                if self.values[right].priority < self.values[idx].priority:
                    if self.values[left].priority > self.values[right].priority:
                        swap_idx = right

            if swap_idx == 0:
                break

            self.values[idx], self.values[swap_idx] = self.values[swap_idx], self.values[idx]
            idx = swap_idx


er = PriorityQueue()
er.enqueue("common cold", 5)
er.enqueue("gunshot wound", 1)
er.enqueue("high fever", 4)
er.enqueue("broken arm", 2)
er.enqueue("glass in foot", 3)
er.enqueue("diarrhea", 3)
print(er)
# [gunshot wound:🔥1, broken arm:🔥2, diarrhea:🔥3, common cold:🔥5, glass in foot:🔥3, high fever:🔥4]

er.dequeue()
print(er)
# [broken arm:🔥2, glass in foot:🔥3, diarrhea:🔥3, common cold:🔥5, high fever:🔥4]

er.dequeue()
print(er)
# [glass in foot:🔥3, high fever:🔥4, diarrhea:🔥3, common cold:🔥5]
