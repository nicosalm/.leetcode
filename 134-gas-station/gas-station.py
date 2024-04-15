class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # n is the circuit size, s is (gas - cost), 
        # t is our gas tank, v is the index of the gas station
        
        n, s, t, v = len(gas), 0, 0, 0 

        for i in range(n):
            s += gas[i] - cost[i]
            t += gas[i] - cost[i]
            if t < 0:
                t = 0 # reset tank
                v = i + 1 # and update starting gas station

        return -1 if (s < 0) else v