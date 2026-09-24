class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltr = []
        rtl = []

        p = 1
        for i in nums:  
            p *= i
            ltr.append(p)
        p = 1
        
        for i in nums[::-1]:
            p *= i
            rtl.append(p)
        rtl = rtl[::-1]
        

        res = []
        n = len(nums)
        for i in range(n):
            p = 1
            p *= ltr[i - 1] if i - 1 >= 0 else 1
            p *= rtl[i + 1] if i + 1 < n else 1

            res.append(p) 
        
        return res