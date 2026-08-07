class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def bt(i):
            
            if len(s) == i:
                res.append(path[:])
                return 
            

            for j in range(i, len(s)):
                if not isPali(s[i:j + 1]):
                    continue
                path.append(s[i:j + 1])
                bt(j + 1)
                path.pop()
        
        def isPali(s):
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True


        bt(0)
        return res