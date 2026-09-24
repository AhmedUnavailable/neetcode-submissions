class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#" + s
        return encoded
        
    def decode(self, s: str) -> List[str]:
        i = 0
        
        res = []
        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1
            
            l = int(s[i:j])
            i = j + 1
            j  = i + l

            
            res.append(s[i:j])
            i = j
        return res
