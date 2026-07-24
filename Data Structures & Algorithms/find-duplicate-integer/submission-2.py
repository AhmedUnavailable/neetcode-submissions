class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        fp = sp = 0
        
        while fp != sp or fp == sp == 0:
            fp = nums[nums[fp]]
            sp = nums[sp]

            
        
        sp2 = 0 
        while sp != sp2:
            sp2 = nums[sp2] 
            sp = nums[sp]
            
        
        return sp2