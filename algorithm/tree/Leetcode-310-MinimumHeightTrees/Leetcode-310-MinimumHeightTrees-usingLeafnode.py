class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1 : return [0]

        dic = collections.defaultdict(list)

        for i in edges :
            a,b = i
            dic[a].append(b)
            dic[b].append(a)

        leaves = []
        for i in range(n+1) :
            if len(dic[i]) == 1 : leaves.append(i)

        while n > 2 : 
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves :
                node = dic[leaf].pop()
                dic[node].remove(leaf)

                if len(dic[node]) == 1 : new_leaves.append(node)

            leaves = new_leaves
        
        return leaves