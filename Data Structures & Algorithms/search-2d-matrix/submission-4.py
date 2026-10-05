class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        t, b = 0, R - 1

        while t <= b:

            m = (t + b) // 2
            
            if matrix[m][0] <= target <= matrix[m][C - 1]:
                l, r = 0, C - 1
                while l <= r:
                    x = (l + r) // 2
                    
                    if matrix[m][x] == target:
                        return True
                    if matrix[m][x] < target:
                        l = x + 1
                    if matrix[m][x] >  target:
                        r = x - 1
                return False


            if matrix[m][C - 1] < target:
                t = m + 1
            if matrix[m][0] > target:
                b = m - 1
        return False
        
            
