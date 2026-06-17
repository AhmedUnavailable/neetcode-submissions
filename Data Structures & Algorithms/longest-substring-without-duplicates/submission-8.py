class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = defaultdict(int)
        start = 0
        res = 0
        for i in range(len(s)):
            if s[i] in hs and hs[s[i]] >= start:
                start = hs[s[i]] + 1
            
            hs[s[i]] = i
            res = max(res, i - start + 1)
                   

        return res
