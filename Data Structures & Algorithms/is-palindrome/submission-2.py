class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = ""
        for i in s:
            if i.isalnum():
                f += i.lower()

        i = 0
        j = len(f) -1
        while(i < j):
            print(f[i], f[j])
            if(f[i] != f[j]):
                return False
            i += 1
            j -= 1
        
        return True
            