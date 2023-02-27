class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for i in range(46)]
        dp[0],dp[1],dp[2],dp[3] = 0, 1, 2, 3
        def myFunc(x): 
            if x <= 0:
                return 0
            elif x == 1:
                return 1
            elif x == 2:
                return 2
            elif x == 3:
                return 3
            else:
                if dp[x] != -1:
                    return dp[x]
                else: 
                    dp[x] = myFunc(x-1) + myFunc(x-2)
                    return dp[x]
        return myFunc(n)