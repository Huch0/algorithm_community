import heapq

class Node:
    def __init__(self, data, list_position, data_position):
        self.data = data
        self.list_position = list_position
        self.data_position = data_position

def merge(input_data):
    def comparator(left, right):
        if left.data == right.data:
            return left.list_position > right.list_position
        return left.data > right.data

    heap = []
    for i, sublist in enumerate(input_data):
        heapq.heappush(heap, Node(sublist[0], i, 0))

    result = []
    while heap:
        min_node = heapq.heappop(heap)
        result.append(min_node.data)
        next_index = min_node.data_position + 1
        if next_index < len(input_data[min_node.list_position]):
            heapq.heappush(heap, Node(input_data[min_node.list_position][next_index], min_node.list_position, next_index))

    return result

if __name__ == "__main__":
    v1 = [1, 3, 8, 15, 105]
    v2 = [2, 3, 10, 11, 16, 20, 25]
    v3 = [-2, 100, 1000]
    v4 = [-1, 0, 14, 18]

    result = merge([v1, v2, v3, v4])

    print(result)
