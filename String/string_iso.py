s = "badc"
t = "baba"

len1 = len(s)
len2 = len(t)

#pat1=s.copy()
#pat2=t.copy()

count1 = 1
count2 = 1

for i in range(len1):
    if len1 != len2:
        print("False")
        break;
    elif i==0:
        count1 = count1 + 1
        count2 = count2 + 1
    else:
        if s[i] == s[i-1]:
            count1 = count1 + 1
        else:
            count1 = 1
        if t[i] == t[i-1]:
            count2 = count2 + 1
        else:
            count2 = 1
    if count1 != count2:
        print("False")
        break;
if count1 == count2:
    print("True")