class MaxBinaryHeap:
    def __init__(self):
        self.values = []

    def __str__(self):
        return str(self.values)

    def insert(self, value):
        self.values.append(value)

        idx = len(self.values) - 1
        parent_idx = (idx - 1) // 2  # parent index of idx

        # Bubbling up the new element to the correct place
        while idx > 0 and self.values[idx] > self.values[parent_idx]:
            # swap parent and child as long as child > parent
            self.values[idx], self.values[parent_idx] = self.values[parent_idx], self.values[idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2

        return self

    def extract_max(self):
        """
        Take out the root (max) element and reorganize the heap to correct order.
        """
        max_value = self.values.pop(0)

        if len(self.values) > 0:
            end = self.values.pop()
            self.values.insert(0, end)
            self.sift_down()

        return max_value

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
                if self.values[left] > self.values[idx]:
                    swap_idx = left

            if right < len(self.values):
                if self.values[right] > self.values[idx]:
                    if self.values[left] < self.values[right]:
                        swap_idx = right

            if swap_idx == 0:
                break

            self.values[idx], self.values[swap_idx] = self.values[swap_idx], self.values[idx]
            idx = swap_idx


heap = MaxBinaryHeap()
heap.insert(99)
heap.insert(2)
heap.insert(3)
heap.insert(33)
heap.insert(1)
heap.insert(1000)
print(heap)  # [1000, 33, 99, 2, 1, 3]
heap.extract_max()
print(heap)  # [99, 33, 3, 2, 1]
heap.extract_max()
print(heap)  # [33, 2, 3, 1]
