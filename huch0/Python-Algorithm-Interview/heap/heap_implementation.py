class BinaryMaxHeap(object):
    def __init__(self) -> None:
        self.items = [None]
        # index 0 is not used for convenience

    def __len__(self) -> int:
        return len(self.items) - 1

    def insert(self, k: int) -> None:
        self.items.append(k)
        self._percolate_up()

    def _percolate_up(self) -> None:
        cur_idx = len(self.items) - 1
        parent_idx = cur_idx // 2

        while parent_idx > 0 and self.items[parent_idx] < self.items[cur_idx]:
            self.items[parent_idx], self.items[cur_idx] = self.items[cur_idx], self.items[parent_idx]

            cur_idx = parent_idx
            parent_idx = cur_idx // 2

    def extract(self) -> int:
        last_idx = len(self.items) - 1
        extracted = self.items[1]
        self.items[1] = self.items[last_idx]
        self.items.pop()
        self._percolate_down(1)

        return extracted

    def _percolate_down(self, idx: int) -> None:
        left_idx = 2 * idx
        right_idx = 2 * idx + 1
        largest_idx = idx

        if left_idx < len(self.items) and self.items[left_idx] > self.items[largest_idx]:
            largest_idx = left_idx

        if right_idx < len(self.items) and self.items[right_idx] > self.items[largest_idx]:
            largest_idx = right_idx

        if idx != largest_idx:
            self.items[idx], self.items[largest_idx] = self.items[largest_idx], self.items[idx]
            idx = largest_idx
            self._percolate_down(idx)


def main():
    max_heap = BinaryMaxHeap()
    max_heap.insert(10)
    max_heap.insert(5)
    max_heap.insert(17)
    max_heap.insert(4)
    max_heap.insert(22)
    max_heap.insert(3)
    max_heap.insert(19)
    max_heap.insert(1)
    max_heap.insert(2)
    max_heap.insert(8)
    max_heap.insert(7)
    max_heap.insert(6)
    max_heap.insert(9)

    print(max_heap.items, "number of items:", len(max_heap))

    while len(max_heap) > 0:
        print(max_heap.extract())
        print(max_heap.items, "number of items:", len(max_heap))


if __name__ == "__main__":
    main()
