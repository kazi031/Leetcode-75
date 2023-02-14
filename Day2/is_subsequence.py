s = "abc"
t = "ahbgdc"

p1 = 0
p2 = 0

while p1 < len(s) and p2 < len(t):
    if s[p1] == t[p2]:
        p1 = p1 + 1
    p2 = p2 + 1

if len(s) == p1:
    print("True")