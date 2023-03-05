class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        myMap = {}
        bulls, cows = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            elif secret[i] in myMap:
                myMap[secret[i]] = 1 + myMap.get(secret[i], 0)
            else:
                myMap[secret[i]] = 1
        for i in range(len(secret)): 
            if guess[i] in myMap and myMap[guess[i]] != 0 and secret[i] != guess[i]:
                cows += 1
                myMap[guess[i]] = myMap.get(guess[i]) - 1
        return str(bulls)+"A"+str(cows)+"B"