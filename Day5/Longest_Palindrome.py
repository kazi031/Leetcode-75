class Solution:
    def longestPalindrome(self, s: str) -> int:
        unique = set()
        x_list = []
        for i in range(len(s)):
            if s[i] not in unique:
                unique.add(s[i])
                x_list.append(s[i])
            else:
                x_list.remove(s[i])
                unique.remove(s[i])
        if len(x_list) == 0:
            return len(s)
        else:
            return len(s)-len(x_list)+1