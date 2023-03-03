class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s = len(s)
        len_p = len(p)
        out = []
        left = 0
        right = len_p - 1
        list_p = list(p)
        list_window = list(s[left:right+1])
        list_p.sort()
        temp_window = list_window.copy()
        temp_window.sort()
        if list_p == temp_window:
            out.append(0)
        left = left + 1
        right = right + 1
        list_window.pop(0)    
        while right < len_s:
            list_window.append(s[right])
            temp_window = list_window.copy()
            temp_window.sort()
            if list_p == temp_window:
                out.append(left)
            left = left + 1
            right = right + 1
            list_window.pop(0)    
            
        return out