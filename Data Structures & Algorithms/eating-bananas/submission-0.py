class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)

        while l <= r:

            m = (l + r) // 2

            hours = h
            for i in piles:
                hours -= math.ceil(i / m)
                if hours < 0:
                    break
            

            if hours < 0:
                l = m + 1
            else:
                r = m - 1
        
        return l
        
        
    



                 



    
