class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s  = set(nums)
        res = 0
        for i in s:
            if i - 1 not in s:
                l = 1
                j = i
                while j + 1 in s:
                    l += 1
                    j += 1
                res = max(res, l)
        return res
