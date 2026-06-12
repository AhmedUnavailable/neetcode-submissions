class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = {}

        for i, v in enumerate(nums):
            hs[v] = i


        

        seqs = []
        for i in nums:
            isMember = False
            for se in seqs:
                if se[0] <= i <= se[1]:
                    isMember = True
            if isMember: continue

            x = i
            while x + 1 in hs :
                x = x + 1
            seqs.append([i, x])    
        
        res = 0
        for seq in seqs:
            res = max(res, seq[1]-seq[0]+1) 
                 
        print(seqs)

        return res