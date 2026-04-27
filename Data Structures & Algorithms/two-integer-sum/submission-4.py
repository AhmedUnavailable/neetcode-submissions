class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        map_prev = {}

        for i, n   in enumerate(nums):
            
            diff = target - n
            if diff in map_prev:
                return [map_prev[diff], i] 
            map_prev[n] = i
    

        