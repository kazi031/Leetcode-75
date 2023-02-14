s = "badc"
t = "baba"

mapST, mapTS = {},{}

for i in range(len(s)):
    c1, c2 = s[i], t[i]

    if((c1 in mapST and mapST[c1] != c2) or
        (c2 in mapST and mapST[c2] != c1)):
        print("False")
    mapST[c1] = c2
    mapTS[c2] = c1
print("True");