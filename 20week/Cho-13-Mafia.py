### 문제 이해
# 1. 딕셔너리 구조로 입력 처리
# 2. 딕셔너리의 정보를 토대로 Tree 구조 구현
# 3. DFS 알고리즘 구현
# 4. 새로운 딕셔너리 구조에 각 노드의 자식 수 저장

from collections import defaultdict

class node:
    def __init__(self, value) -> None:
        self.value = value
        self.parent = None
        self.childrens = []
        self.depth = 0

    def set_parent(self, parent):
        self.parent = parent
    
    def set_child(self, child):
        self.childrens.append(child)

    def set_depth(self, depth):
        self.depth = depth

class Tree:
    def __init__(self) -> None:
        self.root = None
        self.nodes = []

    def make(self, parent, childrens):
        def is_in_nodes(value):
            for i in range(len(self.nodes)):
                if self.nodes[i].value == value:
                    return i
            return -1
            
        par_node = node(parent)
        # 이미 트리에 속한 노드의 경우
        index = is_in_nodes(parent)
        if index >= 0:
            # print(index)
            # for i in range(len(self.nodes)):
            #     print(self.nodes[i].value, end=" ")
            # print("---------------")
            par_node = self.nodes[index]

        for child in childrens:
            ch_node = node(child)
            ch_in = is_in_nodes(child)
            if ch_in >= 0:
                ch_node = self.nodes[ch_in]
            ch_node.set_parent(par_node)
            if ch_in >= 0:
                self.nodes[ch_in] = ch_node
            else:  
                self.nodes.append(ch_node)
            par_node.set_child(ch_node)

        if is_in_nodes(parent) < 0:
            self.nodes.append(par_node)
        

    def set_root(self):
        for node in self.nodes:
            if node.parent == None:
                self.root = node
                return node
            
    def dfs(self, start_node):
        if start_node.childrens is []:
            return 0
        
        result = 0
        for child in start_node.childrens:
            result += self.dfs(child)
        return result + len(start_node.childrens)
    
    def depth(self, target_node, depth):
        if target_node.parent == None:
            return depth
        return self.depth(target_node.parent, depth+1)

class Solution:
    def Mafia(self, file_name):        
        infile = open(file_name, "r")
        N = int(infile.readline().rstrip())
        # 1. 딕셔너리 구조로 입력 처리
        mafia = defaultdict(list)

        for line in infile:
            line = line.split()
            mafia[line[1]].append(line[0])

        infile.close()

        #print(mafia)
        myTree = Tree()
        # 2. 딕셔너리 정보를 토대로 Tree 구조 구현
        for key, value in mafia.items():
            myTree.make(key, value)

        #for node in myTree.nodes:
            #print(node.value)
        # 3. 각 노드 별로 dfs 알고리즘 호출
        # 4. 새로운 딕셔너리 구조에 각 노드의 자식 수 저장
        results = {}

        for node in myTree.nodes:
            #print(node.value + " and len: " + str(len(node.childrens)))
            count = myTree.dfs(node)
            depth = myTree.depth(node, 0)
            results[node.value] = (count, depth)
        
        # 5. 자식 수, 알파벳 기준으로 정렬 후 출력
        results = dict(sorted(results.items(), key=lambda item: (-item[1][0], item[1][1], item[0])))
        outputs = []
        #print(results)
        for name in results:
            outputs.append(name)
        return outputs

### TEST CODE
if __name__ == "__main__":
    s = Solution()
    #print(s.Mafia("Cho-13-Test/02.inp"))
    for i in range(1, 10):
        input_file_name = "Cho-13-Test/0" + str(i) + ".inp"
        result_file_name = "Cho-13-Test/0" + str(i) + ".out"
        
        infile = open(result_file_name, "r")
        
        results = s.Mafia(input_file_name)

        outputs = []
        
        for line in infile:
            outputs.append(line.rstrip())

        infile.close()
        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")
    
    for i in range(10, 16):
        input_file_name = "Cho-13-Test/" + str(i) + ".inp"
        result_file_name = "Cho-13-Test/" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        results = s.Mafia(input_file_name)

        outputs = []
        
        for line in infile:
            outputs.append(line.rstrip())

        infile.close()
        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")