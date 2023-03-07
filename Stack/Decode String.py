class Solution:
    def decodeString(self, s: str) -> str:
        out_str = []
        digit = 0
        for i in range(len(s)):
            if s[i] != "]":
                out_str.append(s[i])
                if s[i].isdigit():
                    digit += 1
            else:
                sub_str = ""
                while out_str[-1] != "[":
                    sub_str = out_str.pop() + sub_str
                out_str.pop()
                n = ""
                while out_str and out_str[-1].isdigit():
                    n = out_str.pop() + n
                n = int(n)
                out_str.append(int(n)*sub_str)
        if digit == len(s):
            return ""
        else:
            return "".join(out_str)
            