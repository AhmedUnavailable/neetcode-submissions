class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        candidates.sort()

        def bt(path, i, s):
             
            if s == target:
                res.append(path[:])
                return
            if i == len(candidates) or s > target:
                return

            path.append(candidates[i])
            bt(path, i + 1, s + candidates[i])
            path.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1] :
                i += 1

            bt(path, i + 1, s)

        bt([], 0, 0) 
        return res