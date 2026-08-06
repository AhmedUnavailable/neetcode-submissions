class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()


        def bt(path, i):
            if i == len(nums):
                res.append(path[:])
                return

            path.append(nums[i])

            

            bt(path, i + 1)

            path.pop()

            while i < len(nums) - 1  and nums[i] == nums[i + 1] :
                i += 1

            bt(path, i + 1)

        bt([], 0)
            
        return res
            