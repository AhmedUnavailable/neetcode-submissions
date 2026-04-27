class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count = [0] * 26
        
        for i in s:
            count[ord(i) - ord("a")] += 1
        for i in t:
            count[ord(i) - ord("a")] -= 1

        return all(i == 0 for i in count)