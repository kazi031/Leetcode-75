class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashMap = {}
        freq = [[] for i in range(len(words) + 1)]
        for word in words:
            if word in hashMap:
                hashMap[word] = 1 + hashMap.get(word, 0)
            else:
                hashMap[word] = 1
        #listMap = list(hashMap.items())
        #heapq.heapify(listMap)
        #print(listMap)
        #SortedhashMap = sorted(hashMap.items(), key=lambda x:x[1])
        for n,c in hashMap.items():
            freq[c].append(n)
        #print(SortedhashMap)
        print(freq)
        outString = []
        for i in range(len(freq)-1, 0, -1):
            if len(freq[i])>0:
                newList = freq[i]
                print(newList)
                #heapq.heapify(newList)
                newList.sort()
                print(newList)
                for n in newList:
                    outString.append(n)
                    #print(outString)
                if len(outString) > k:
                    while len(outString) != k:
                        outString.pop()
                    return outString
                elif len(outString) == k:
                    return outString