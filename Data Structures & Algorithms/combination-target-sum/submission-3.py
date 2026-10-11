class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(path, s, idx):
            if s > target:
                return 
            if s == target:
                res.append(path[:])

            for i in range(idx, len(nums)):
                path.append(nums[i])
                dfs(path, s + nums[i], i )
                path.pop()
                
                
        dfs([], 0, 0)

        return res
            
            