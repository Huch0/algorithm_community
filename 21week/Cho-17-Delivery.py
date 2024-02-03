### 문제 이해
# 1.2차원 map을 Graph 구조로 바꾸는 것이 중요
# 위에 대한 해답으로 (value, row, column)과 같은 Triple 객체를 노드로 만들고
# 위 노드를 Vertex로 하여 각 노드와 edge로 연결



# 4. 시간 계산 함수 구현
# 5. 결과 반환

from collections import defaultdict

class Node:
    def __init__(self, value, row, column) -> None:
        self.value = value
        self.row = row
        self.column = column
    def __str__(self):
        return f"({self.row}, {self.column})"

class Graph:
    def __init__(self, N, T):
        self.N = N
        self.node_list = []
        self.edge_list = defaultdict(list)
        self.path_list = []
        self.min_path_length = 100000
        self.visited = set()  # 변경: 리스트에서 세트로 변경
        self.T = T

    def add_nodes(self, list, row):
        for i in range(self.N):
            self.node_list.append(Node(list[i], row, i))
    
    def get_node(self, row, column):
        if row < 0 or row >= self.N or column < 0 or column >= self.N:
            return None
        for node in self.node_list:
            if node.row == row and node.column == column:
                return node
        
    def set_edge(self):
        for node in self.node_list:
            self.edge_list[str(node)].append(self.get_node(node.row+1, node.column))
            self.edge_list[str(node)].append(self.get_node(node.row, node.column+1))
            self.edge_list[str(node)].append(self.get_node(node.row-1, node.column))
            self.edge_list[str(node)].append(self.get_node(node.row, node.column-1))
    
    def cal_path_length(self, path):
        def cal_length(p1, p2):
            p1 = p1[1:-1].split(',')
            p2 = p2[1:-1].split(',')

            return abs(int(p2[1])-int(p1[1])) + abs(int(p2[0])-int(p1[0]))
        
        length = 0
        for i in range(len(path)-1):
            length += cal_length(str(path[i+1]), str(path[i]))

        return length + self.T*(len(path)-2)

    def dfs(self, start, path):
        #print(start)
        # 종료 시점
        if start.row == 0 and start.column == self.N-1:
            path.append(start)
            print(path)
            if self.cal_path_length(path) < self.min_path_length:
                self.path_list.append(path.copy())
                self.min_path_length = self.cal_path_length(path)
            return

        # DFS 재귀로 동작
        for neighbor in self.edge_list[str(start)]:
            if neighbor and neighbor not in self.visited and neighbor.value == 0:
                self.visited.add(neighbor)
                if neighbor.row != path[-1].row and neighbor.column != path[-1].column:   
                    self.dfs(neighbor, path + [start])
                else:
                    self.dfs(neighbor, path)
                self.visited.remove(neighbor)

class Solution:
    def Delivery(self, file_name):
        # 1. 입력 처리
        infile = open(file_name, "r")
        first_line = [int(num) for num in infile.readline().split()]
        N, T = first_line[0], first_line[1]
        graph = Graph(N, T)

        row = 0
        for line in infile:
            graph.add_nodes([int(num) for num in line.split()], row)
            row += 1
        infile.close()

        start_node = Node(0, N-1, 0)
        graph.set_edge()
        graph.dfs(start_node, [start_node])
        for path in graph.path_list:
            for node in path:
                print(node, end = ' ')
        print(graph.cal_path_length(graph.path_list[-1]))
        # 3. 각 path들의 꼭짓점을 보고 걸린 시간 계산하기
        

### TEST CODE
if __name__ == "__main__":
    s = Solution()
    s.Delivery("Cho-17-Test/01.inp")
    # for i in range(1, 10):
    #     input_file_name = "Cho-15-Test/0" + str(i) + ".inp"
    #     result_file_name = "Cho-15-Test/0" + str(i) + ".out"
        
    #     infile = open(result_file_name, "r")
        
    #     results = s.Party(input_file_name)

    #     outputs = (infile.readline().rstrip(), int(infile.readline().rstrip()))

    #     infile.close()
    #     if results == outputs:
    #         print("CORRECT")
    #     else:
    #         print("INCORRECT")
    
    # for i in range(10, 16):
    #     input_file_name = "Cho-15-Test/" + str(i) + ".inp"
    #     result_file_name = "Cho-15-Test/" + str(i) + ".out"

    #     infile = open(result_file_name, "r")
        
    #     results = s.Party(input_file_name)

    #     outputs = (infile.readline().rstrip(), int(infile.readline().rstrip()))

    #     infile.close()
    #     if results == outputs:
    #         print("CORRECT")
    #     else:
    #         print("INCORRECT")