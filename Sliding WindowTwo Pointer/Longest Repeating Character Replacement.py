class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #hashmap
        result = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            if (right-left+1-max(count.values())) <= k:
                result = max(result, right-left+1)
            else:
                count[s[left]] -= 1
                left = left + 1
        return result
