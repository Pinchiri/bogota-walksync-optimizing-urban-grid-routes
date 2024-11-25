class BinaryHeap:
    def __init__(self):
        self.heap = []

    def heappush(self, item):
        """Inserts an item into the heap."""
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def heappop(self):
        """Removes and returns the smallest item from the heap."""
        if not self.heap:
            raise IndexError("Heap is empty")
        smallest = self.heap[0]
        end_item = self.heap.pop()
        if self.heap:
            self.heap[0] = end_item
            self._sift_down(0)
        return smallest

    def _sift_up(self, idx):
        """Moves the item at index idx up to its correct position."""
        item = self.heap[idx]
        while idx > 0:
            parent_idx = (idx - 1) >> 1
            parent = self.heap[parent_idx]
            if item < parent:
                self.heap[idx] = parent
                idx = parent_idx
            else:
                break
        self.heap[idx] = item

    def _sift_down(self, idx):
        """Moves the item at index idx down to its correct position."""
        end_idx = len(self.heap)
        item = self.heap[idx]
        child_idx = 2 * idx + 1  # Left child index
        while child_idx < end_idx:
            # Right child index
            right_idx = child_idx + 1
            # Select the smaller of the two children
            if right_idx < end_idx and self.heap[right_idx] < self.heap[child_idx]:
                child_idx = right_idx
            # If the child is smaller than the item
            if self.heap[child_idx] < item:
                self.heap[idx] = self.heap[child_idx]
                idx = child_idx
                child_idx = 2 * idx + 1
            else:
                break
        self.heap[idx] = item

    def __bool__(self):
        """Returns True if the heap is not empty."""
        return bool(self.heap)
