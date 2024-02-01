### 문제 이해
# 1. 입력 처리: 각 입력을 networkX를 이용해서 노드로 만들고 그래프 생성
# 2. 각 노드별로 친구들까지의 거리를 계산해서 max값을 가진다. 이를 딕셔너리로 저장한다
# 3. 위 결과를 출력한다.

import networkx as nx

class Solution:
    def Party(self, file_name):
        # 1. 입력 처리
        infile = open(file_name, "r")

        N = int(infile.readline())
        friends = infile.readline().split()
        graph_info = []

        for line in infile:
            graph_info.append(line.split())

        infile.close()
        
        # 2. 그래프 구조 구현
        G = nx.Graph()
        nodes = []
        edges = []
        for graph in graph_info:
            nodes.append(graph[0])
            for target_node in graph[1:-1]:
                if (target_node, graph[0], {'weight': 1}) not in edges:
                    edges.append((graph[0], target_node, {'weight': 1}))

        G.add_nodes_from(nodes)
        G.add_edges_from(edges)#[(1, 2, {'weight': 1}), (2, 3, {'weight': 2}), (3, 4, {'weight': 1}), (1, 4, {'weight': 3})])

        # 3. 각 노드별 친구들과의 거리를 계산 후 딕셔너리에 저장
        distance = {}
        for node in G.nodes:
            max_path_length = -1
            for f_node in friends:
                try:
                    # Dijkstra 알고리즘으로 최단 경로 계산
                    shortest_path = nx.shortest_path_length(G, source=node, target=f_node, weight='weight')
                    # vertex를 지날 때 2분을 고려
                    if shortest_path != 0:
                        shortest_path += 2*(shortest_path-1)
                    #print(f"{node} -> {f_node} len : {shortest_path}")
                    max_path_length = max(max_path_length, shortest_path)
                except nx.NetworkXNoPath:
                    max_path_length = -1
                    
            #print()
            distance[node] = max_path_length

        outputs = sorted(distance.items(), key=lambda x: (x[1], x[0]))
        if outputs[0][1] == -1:
            return ('@', -1)
        return outputs[0]

### TEST CODE
if __name__ == "__main__":
    s = Solution()
    print(s.Party("Cho-15-Test/01.inp"))
    for i in range(1, 10):
        input_file_name = "Cho-15-Test/0" + str(i) + ".inp"
        result_file_name = "Cho-15-Test/0" + str(i) + ".out"
        
        infile = open(result_file_name, "r")
        
        results = s.Party(input_file_name)

        outputs = (infile.readline().rstrip(), int(infile.readline().rstrip()))

        infile.close()
        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")
    
    for i in range(10, 16):
        input_file_name = "Cho-15-Test/" + str(i) + ".inp"
        result_file_name = "Cho-15-Test/" + str(i) + ".out"

        infile = open(result_file_name, "r")
        
        results = s.Party(input_file_name)

        outputs = (infile.readline().rstrip(), int(infile.readline().rstrip()))

        infile.close()
        if results == outputs:
            print("CORRECT")
        else:
            print("INCORRECT")