class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += f"{len(s)}#{s}"
        return enc


    def decode(self, s: str) -> List[str]:
        print(s)               
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            print(s[i:j])
            l = int(s[i:j])

            i = j + 1
            j = i + l 
        
            res.append(s[i:j])
            i = j
            
        return res 
