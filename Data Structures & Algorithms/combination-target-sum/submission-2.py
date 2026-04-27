class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def bt(path, idx):
            tot = sum(path) 
            if  tot == target:
                res.append(path[:])
                return
            if tot > target:
                return
            if idx == len(nums):
                return

            path.append(nums[idx])
            bt(path, idx)
            path.pop()
            bt(path, idx + 1)


        bt([], 0)
        return res