class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        
        counts = defaultdict(int)

        res = 0

        for r in range(len(s)):
            counts[s[r]] += 1

            max_char = max(counts, key=counts.get)
            max_count = counts[max_char]



            while r - l + 1 - max_count > k:
                counts[s[l]] -= 1
                l += 1

            res = max(r - l + 1, res)

        return res