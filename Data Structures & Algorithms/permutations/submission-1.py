class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []


        def bt(path, s):
            if len(path) == len(nums):
                res.append(path[:])
            
            for i in nums:
                if i in s:
                    continue
                
                path.append(i)
                s.add(i)
                bt(path, s)

                path.pop()
                s.remove(i)
            
        
        bt([], set())
        return res