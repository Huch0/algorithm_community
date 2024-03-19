class Solution(object):
    def combine(self, n, k):
        results = []
        def dfs(comb, start):
            #base case
            if len(comb) == k:
                results.append(comb[:])
                return

            for i in range(start, n+1):
                comb.append(i)
                dfs(comb,i+1)
                comb.pop()
            
        dfs([],1)
        return results

        #return list(itertools.combinations(range(1,n+1), k))
        