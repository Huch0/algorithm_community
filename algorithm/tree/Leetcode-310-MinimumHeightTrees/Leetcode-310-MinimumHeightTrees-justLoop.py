class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1 : return [0]

        dic = collections.defaultdict(list)

        for i in edges :
            a,b = i
            dic[a].append(b)
            dic[b].append(a)

        nodes = dic.keys()
        
        while n > 2 :

            node = []
            leave_node = []
            for i in nodes :
                if len(dic[i]) == 1 : 
                    leave_node.append(i)
                else : node.append(i)
            
            for i in leave_node :
                dic[dic[i][0]].remove(i)

            nodes = node
            n = len(nodes)
        
        return nodes