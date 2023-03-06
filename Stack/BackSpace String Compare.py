class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        len_c = 0
        if len(s) >= len(t):
            for i in range(len(s)):
                if s[i] != "#":
                    stack1.append(s[i])
                else:
                    if len(stack1) != 0: 
                        stack1.pop()
                if len_c < len(t):
                    if t[len_c] != "#":
                        stack2.append(t[len_c])
                    else:
                        if len(stack2) != 0: 
                            stack2.pop()
                    len_c += 1
        else:
            for i in range(len(t)):
                if t[i] != "#":
                    stack2.append(t[i])
                else:
                    if len(stack2) != 0:
                        stack2.pop()
                if len_c < len(s):
                    if s[len_c] != "#":
                        stack1.append(s[len_c])
                    else: 
                        if len(stack1) != 0: 
                            stack1.pop()
                    len_c += 1  

        if stack1 == stack2:
            return True
        else:
            return False