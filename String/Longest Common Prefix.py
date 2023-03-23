class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        num = len(strs)
        str1 = strs[0]
        count = 0
        str1_len = len(str1)
        for i in range(str1_len):
            letter = str1[i];
            total = 1
            for j in range(1,num):
                temp_str = strs[j]
                if i > (len(temp_str) - 1):
                    break;
                elif temp_str[i] == letter:
                    total = total + 1
                else: break;
            if total == num:
                count = count + 1;
            else: break;
        return str1[0:count]