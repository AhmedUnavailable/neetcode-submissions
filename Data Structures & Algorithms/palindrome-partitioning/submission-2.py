class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        divs = []
        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def bt(i):
            if i >= len(s):
                
                res.append(divs[:])
                return
            
            for j in range(i, len(s)):
                if isPali(i, j):
                    divs.append(s[i:j + 1])
                    bt(j + 1)
                    divs.pop()
                

        bt(0)
        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        return res
