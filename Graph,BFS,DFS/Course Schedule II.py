class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqList = {c:[] for c in range(numCourses)}
        
        for crs, pre in prerequisites:
            prereqList[crs].append(pre)
        
        visit, cycle = set(), set()
        outArr = []
        def dfs(course):
            if course in cycle:
                return False
            elif course in visit:
                return True
            cycle.add(course)

            for pre in prereqList[course]:
                if dfs(pre) == False:
                    return False
            cycle.remove(course)
            visit.add(course)
            outArr.append(course)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        
        return outArr