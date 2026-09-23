class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

            

        for s in strs:
            arr = [0]*26
            for c in s:
                arr[ord("a")-ord(c)] += 1
            
            
            d[tuple(arr)].append(s)
        
        return list(d.values())


            