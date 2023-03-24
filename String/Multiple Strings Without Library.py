class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        value = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        total1 = 0
        for i in range(len(num1)):
            temp = ord(num1[i]) - ord("0")
            total1 = total1 + temp * pow(10, len(num1)-i-1)
        total2 = 0
        for i in range(len(num2)):
            temp = ord(num2[i]) - ord("0")
            total2 = total2 + temp * pow(10, len(num2)-i-1)
        total = total1 * total2
        out_str = ""
        if total == 0:
            out_str = "0" + out_str
        while(total != 0):
            x = total % 10
            temp = value[x]
            out_str = temp + out_str
            total = total//10
        return out_str