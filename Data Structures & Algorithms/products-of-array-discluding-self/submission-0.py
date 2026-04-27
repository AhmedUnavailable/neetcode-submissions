class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ftb = []
        temp = 1
        for i in nums:         
            temp *= i
            ftb.append(temp)
        btf = []

        temp = 1
        for i in nums[::-1]:         
            temp *= i
            btf.append(temp)
        btf = btf[::-1]
        
        print(ftb, btf)

        res = []
        for i in range(len(nums)):
            temp  = 1
            
            if (i - 1) >= 0:
                print(nums[i])
                temp *= ftb[i - 1]
            if (i + 1) < len(nums):
                temp *= btf[i + 1]
            
            res.append(temp)

        return res