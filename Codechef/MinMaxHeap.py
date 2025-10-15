class MinMaxHeap:
    """
    A conceptual implementation of a Min-Max Heap in Python.
    Uses a list to represent the binary tree structure.
    """
    def __init__(self):
        # Heap stored in a list, index 0 is unused (standard practice)
        self.heap = [0]
        self.size = 0

    def _is_min_level(self, i):
        """
        Determines if an index i is on a min-level (level 0, 2, 4, ...).
        Level is log2(i) floored.
        """
        if i == 0:
            return False # Root is at index 1
        # Level of node i (1-based index) is floor(log2(i))
        # An easier check is to see if the level number is even.
        import math
        level = math.floor(math.log2(i))
        return level % 2 == 0

    def _parent(self, i):
        return i // 2

    def _left_child(self, i):
        return 2 * i

    def _right_child(self, i):
        return 2 * i + 1

    # --- Insertion ---
    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self._bubble_up(self.size)

    def _bubble_up(self, i):
        if i == 1: # Root
            return

        parent_i = self._parent(i)
        
        # Check if i is on a min level
        if self._is_min_level(i):
            # i is on a Min-Level: Check if item is > parent (Violation)
            if self.heap[i] > self.heap[parent_i]:
                # Violates min property: swap with parent and bubble up max-level
                self.heap[i], self.heap[parent_i] = self.heap[parent_i], self.heap[i]
                self._bubble_up_max(parent_i)
            # Otherwise, item is <= parent: bubble up min-level
            else:
                self._bubble_up_min(i)

        # Check if i is on a max level
        else: # Max-Level
            # i is on a Max-Level: Check if item < parent (Violation)
            if self.heap[i] < self.heap[parent_i]:
                # Violates max property: swap with parent and bubble up min-level
                self.heap[i], self.heap[parent_i] = self.heap[parent_i], self.heap[i]
                self._bubble_up_min(parent_i)
            # Otherwise, item is >= parent: bubble up max-level
            else:
                self._bubble_up_max(i)

    def _bubble_up_min(self, i):
        """Standard min-heap bubble up, but checking grandparents."""
        grandparent_i = self._parent(self._parent(i))
        if grandparent_i >= 1:
            if self.heap[i] < self.heap[grandparent_i]:
                self.heap[i], self.heap[grandparent_i] = self.heap[grandparent_i], self.heap[i]
                self._bubble_up_min(grandparent_i)

    def _bubble_up_max(self, i):
        """Standard max-heap bubble up, but checking grandparents."""
        grandparent_i = self._parent(self._parent(i))
        if grandparent_i >= 1:
            if self.heap[i] > self.heap[grandparent_i]:
                self.heap[i], self.heap[grandparent_i] = self.heap[grandparent_i], self.heap[i]
                self._bubble_up_max(grandparent_i)
    
    # --- Retrieval ---
    def get_min(self):
        """Minimum element is always the root (index 1)."""
        if self.size < 1:
            raise IndexError("Heap is empty.")
        return self.heap[1]

    def get_max(self):
        """
        Maximum element is the larger of the root's children (indices 2 or 3).
        If only one child exists (index 2), that is the max.
        """
        if self.size < 1:
            raise IndexError("Heap is empty.")
        if self.size == 1:
            return self.heap[1]
        if self.size == 2:
            return self.heap[2]
        
        # Max is max(root's children)
        return max(self.heap[2], self.heap[3])

    # --- Deletion (Min) ---
    def delete_min(self):
        if self.size < 1:
            raise IndexError("Heap is empty.")
        
        # 1. Swap the root (min) with the last element
        min_val = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.size -= 1
        
        # 2. Bubble the new root down
        if self.size > 0:
            self._trickle_down(1)
            
        return min_val
        
    def _trickle_down(self, i):
        # A full trickle_down implementation is the most complex part
        # and requires finding the minimum grandchild or child to swap with.
        
        # NOTE: Full implementation is lengthy. This is a simplified outline.
        # It needs to find the smallest of children/grandchildren 'm'
        # and perform the appropriate swap and subsequent trickle.
        pass # Placeholder for complex trickle-down logic

    def __str__(self):
        return f"Size: {self.size}, Heap: {self.heap[1:]}"
        
# --- Example Usage ---
mm_heap = MinMaxHeap()
elements = [10, 8, 30, 2, 50, 15, 60]
for x in elements:
    mm_heap.insert(x)

print(f"Heap after insertions: {mm_heap}")
print(f"Min element: {mm_heap.get_min()}")
print(f"Max element: {mm_heap.get_max()}")

# mm_heap.delete_min() # Requires full _trickle_down implementation
# print(f"Heap after delete_min: {mm_heap}")
