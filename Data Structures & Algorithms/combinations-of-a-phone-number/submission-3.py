class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        if not digits:
            return []

        keyLetters = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def bt(path, i):
            if len(digits) == len(path):
                res.append(path)
                return

            for j in keyLetters[digits[i]]:
                
                bt(path + j, i + 1)
                

        bt("", 0)
        
        return res 

