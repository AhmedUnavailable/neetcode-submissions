class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for n in nums:
            freqs[n] += 1
        
        rev = [[] for i in range(len(nums) + 1)]

        for i in freqs:
            rev[freqs[i]].append(i)
        
        res = []
        for i in rev[::-1]:
            res = res + i
            if len(res) >= k:
                return res     
        
        

        