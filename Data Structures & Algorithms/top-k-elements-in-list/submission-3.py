class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for i in nums:
            freqs[i] += 1

        print(freqs)
        hm = [[] for i in range(len(nums) + 1)]

        for n, c in freqs.items():
            hm[c].append(n)
        
        print(hm)
        res = []
        for i in hm[::-1]:
        
            for x in i:
                res.append(x)
                if len(res) == k:
                    return res
        
       

        