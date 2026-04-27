class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        

        for s in strs:
            hash_set = 26*[0]
            for i in s:
                hash_set[ord(i)-ord("a")] += 1
            
            groups[str(hash_set)].append(s)

        
        return list(groups.values())