83 186 408 419
amount = 6249

14

Greedy Doesn't Work:

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = 0
        coins.sort()
        for i in range(len(coins)-1, -1, -1):
            if amount % coins[i] == 0:
                div = amount // coins[i]
                res = res + div
                return res
            else:
                if amount > coins[i]:
                    div = amount // coins[i]
                    if amount - div * coins[i] > 0:
                        amount = amount - div * coins[i]
                        res = res + div
        return -1
