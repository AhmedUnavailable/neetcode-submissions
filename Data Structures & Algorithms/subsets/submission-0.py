class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtracking(path, idx):
            
            if idx == len(nums):
                res.append(path[:])
                return
            
            path.append(nums[idx])
            backtracking(path, idx + 1)
            path.pop()

            backtracking(path, idx + 1)

            


        backtracking([], 0)
        return res
            

        