class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const prevList = new Map()
        for (let i = 0; i < nums.length ; i++){
            const diff = target - nums[i]
            
            if(prevList.has(diff)){
                return [prevList.get(diff), i]
            }
            prevList.set(nums[i], i)
        }  
        return []
    }
}
