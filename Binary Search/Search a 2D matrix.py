class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1


        while(top < bottom):
            if matrix[bottom][0] > target:
                bottom -= 1
            elif matrix[top][len(matrix[0])-1] < target:
                top += 1

        while left<=right:
            middle = (left+right)//2
            if matrix[top][middle] == target:
                return True
            elif matrix[top][middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return False