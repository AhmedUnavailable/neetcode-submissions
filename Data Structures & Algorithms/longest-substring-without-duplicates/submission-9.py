class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = defaultdict(int)
        res = 0
        start = 0

        for i in range(len(s)):
            if s[i] in hs and hs[s[i]] >= start:
                start = hs[s[i]] + 1
            
            hs[s[i]] = i
            res = max(i -  start + 1, res)
        
        return res