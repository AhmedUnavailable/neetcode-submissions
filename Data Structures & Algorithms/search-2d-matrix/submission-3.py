class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1

        
        while t <= b:
            m = (t + b) // 2
            m_row = matrix[m]
            
            if target > m_row[-1]:
                t = m + 1
            elif target < m_row[0]:
                b = m - 1
            else:
                break

        if not (t <= b):
            return False

        row = matrix[(t + b) // 2]

        print(row)

        l, r = 0, len(row) - 1
    
        while l <= r:
            m = (l + r) // 2


            if row[m] > target:
                r = m - 1
            elif row[m] < target:
                l = m + 1
            else:
                return True

        return False


        