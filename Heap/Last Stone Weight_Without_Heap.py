class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            findMax = max(stones)
            print(findMax)
            stones.remove(findMax)
            SecMax = max(stones)
            print(SecMax)
            if findMax == SecMax:
                stones.remove(SecMax)
            else:
                stones.remove(SecMax)
                stones.append(findMax-SecMax)
        
        if len(stones) == 1:
            return stones[0]
        else:
            return 0

