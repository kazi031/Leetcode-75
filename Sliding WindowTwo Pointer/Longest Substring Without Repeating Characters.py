class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        CharSet = set()
        left = 0
        result = 0

        for right in range(len(s)):
            while s[right] in CharSet:
                CharSet.remove(s[left])
                left += 1
            CharSet.add(s[right])
            result = max(result, right - left + 1)
        return result