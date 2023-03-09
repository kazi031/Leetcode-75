class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            FindMax = heapq.heappop(stones)
            SecMax = heapq.heappop(stones)
            if FindMax < SecMax:
                heapq.heappush(stones, FindMax - SecMax)
        stones.append(0)
        return abs(stones[0])
