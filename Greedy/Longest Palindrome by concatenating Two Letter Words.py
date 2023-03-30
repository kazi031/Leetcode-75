class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        wordCount = {}
        length = 0

        numRepeat = 0

        for word in words:
            if word[::-1] in wordCount:
                length += 4
                wordCount[word[::-1]] -= 1
                if wordCount[word[::-1]] == 0:
                    wordCount.pop(word[::-1])
                if word[0] == word[1]:
                    numRepeat -= 1
                continue
                
            wordCount[word] = 1 + wordCount.get(word,0)
            if word[0] == word[1]:
                numRepeat += 1
        
        if numRepeat > 0:
            return length + 2
        else:
            return length