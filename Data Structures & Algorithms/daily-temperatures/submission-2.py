class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        s = []
        for i, temp in enumerate(temperatures):
            while s and temp > s[-1][1] :
                a = s.pop()
                res[a[0]] = i - a[0]
            
            s.append((i,temp))
        

        return res