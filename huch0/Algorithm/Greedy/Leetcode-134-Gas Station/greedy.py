class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start, tank = 0, 0

        for i in range(len(gas)):
            if gas[i] + tank < cost[i]:
                start = i + 1
                tank = 0
            else:
                tank += gas[i] - cost[i]

        return start
