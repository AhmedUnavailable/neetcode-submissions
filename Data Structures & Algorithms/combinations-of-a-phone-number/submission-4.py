class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs' ,
            '8': 'tuv',
            '9': "wxyz"
        }
        res = []

        def bt(path,i):
            if len(path) == len(digits):
                res.append(path)
                return
            for c in hm[digits[i]]:
                bt(path + c, i + 1)
        
        if digits:        
            bt('', 0)
        return res
