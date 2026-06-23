class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        l, r = 0, 0

        s1_map = defaultdict(int)

        for i in s1:
            s1_map[i] += 1
        
        window_map = defaultdict(int)
        for r in range(len(s2)):
            window_map[s2[r]] += 1


            if all( window_map[x] == s1_map[x] for x in s1_map):
                return True

            if r - l + 1 >= n:
                window_map[s2[l]] -= 1
                l += 1
                
            
            
        return False
  

        
        
            