class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        fuel = []

        for i in range(len(gas)) :
            fuel.append(gas[i]-cost[i])

        if sum(fuel) < 0 : return -1

        print(fuel)
        start = 0
        fuel_sum = 0
        for i in range(len(fuel)) :
            fuel_sum += fuel[i]
            if fuel_sum < 0 : 
                start = i+1
                fuel_sum = 0
        return start