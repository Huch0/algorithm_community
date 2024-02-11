class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network = collections.defaultdict(list)

        for u,v,time in times :
            network[u].append((v,time))
        
        heap = [(0,k)]
        dic = collections.defaultdict(int)

        while heap :
            pop = heappop(heap)
            if pop[1] not in dic :
                dic[pop[1]] = pop[0]
                for v, time in network[pop[1]] :
                    times = pop[0] + time
                    heappush(heap,(times,v))
    
        print(dic)
        if len(dic) == n : return max(dic.values())
        else : return -1