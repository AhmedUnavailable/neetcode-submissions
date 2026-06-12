class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        res =0
        for i in nums:
            if i - 1 not in hs:
                length = 1
                
                while i + length in hs :
                    length  += 1
                
                res = max(length, res)
        

        return res