class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            count = [0]*26
            for c in i:
                count[ord(c) - ord("a")] += 1
            
            result[tuple(count)].append(i) 
            
        return list(result.values())    
                
            




    def isAnagram(a, t):
        if len(a) != len(t):
            return False

        countA, countT ={}, {}
        for i in range(len(a)):
            countA[a[i]] = 1 + countA.get(a[i])
            countT[t[i]] = 1 + countT.get(t[i])
        return countA == countT 
            
        