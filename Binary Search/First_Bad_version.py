class Solution:
    def firstBadVersion(self, n: int) -> int:
        num = n
        l,r = 1, num
        while l<=r:
            middle = (l+r)//2
            if l == r:
                return l
            elif isBadVersion(middle) == True:
                if isBadVersion(middle-1) == False:
                    return middle
                r = middle - 1
            elif isBadVersion(middle) == False:
                l = middle + 1
        return l