class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(path, idx):
            if idx > len(nums) - 1:
                res.append(path[:])
                return

            path.append(nums[idx])
            
            bt(path, idx + 1)

            path.pop()

            bt(path, idx + 1)
        bt([], 0)

        return res
            
