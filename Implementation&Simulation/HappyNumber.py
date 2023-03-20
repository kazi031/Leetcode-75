class Solution:
    def isHappy(self, n: int) -> bool:
        loop_check = set()
        def happyCheck(n: int) -> bool:
            x = str(n)
            total = 0
            #if len(x) == 1 and n != 1:
            #    return False
            for i in range(len(x)):
                conv = int(x[i])
                total = total + conv * conv
            
            if total == 1:
                return True
            elif total in loop_check:
                return False
            else:
                loop_check.add(total) 
                return happyCheck(total)
        return happyCheck(n)