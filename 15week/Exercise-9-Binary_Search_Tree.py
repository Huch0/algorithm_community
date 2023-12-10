class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def find(self, value):
        return self._finder(self.root, value)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._inserter(self.root, value)

    def inorder(self):
        self._inorder_traversal(self.root)
        print()

    def successor(self, start):
        current = start.right
        while current and current.left:
            current = current.left
        return current

    def delete_value(self, value):
        self.root = self._deleter(self.root, value)

    def _finder(self, current, value):
        if not current:
            print()
            return None

        if current.data == value:
            print(f"{value}을(를) 찾았습니다.")
            return current
        elif value < current.data:
            print(f"{current.data}에서 왼쪽으로 이동: ", end="")
            return self._finder(current.left, value)
        else:
            print(f"{current.data}에서 오른쪽으로 이동: ", end="")
            return self._finder(current.right, value)

    def _inserter(self, current, value):
        if value <= current.data:
            if not current.left:
                current.left = Node(value)
            else:
                self._inserter(current.left, value)
        else:
            if not current.right:
                current.right = Node(value)
            else:
                self._inserter(current.right, value)

    def _inorder_traversal(self, start):
        if not start:
            return

        self._inorder_traversal(start.left)
        print(start.data, end=" ")
        self._inorder_traversal(start.right)

    def _deleter(self, start, value):
        if not start:
            return None

        if value < start.data:
            start.left = self._deleter(start.left, value)
        elif value > start.data:
            start.right = self._deleter(start.right, value)
        else:
            if not start.left:
                tmp = start.right
                del start
                return tmp
            if not start.right:
                tmp = start.left
                del start
                return tmp

            succ_node = self.successor(start)
            start.data = succ_node.data
            start.right = self._deleter(start.right, succ_node.data)

        return start


if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(12)
    tree.insert(10)
    tree.insert(20)
    tree.insert(8)
    tree.insert(11)
    tree.insert(15)
    tree.insert(28)
    tree.insert(4)
    tree.insert(2)

    print("중위 순회:", end=" ")
    tree.inorder()

    tree.delete_value(12)
    print("12를 삭제한 후 중위 순회:", end=" ")
    tree.inorder()

    if tree.find(12):
        print("원소 12는 트리에 있습니다.")
    else:
        print("원소 12는 트리에 없습니다.")
