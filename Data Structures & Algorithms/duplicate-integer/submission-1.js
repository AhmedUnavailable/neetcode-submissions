class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const seen = new Set()
        for (let e of nums){
            if (seen.has(e)){
                return true     
            }
            seen.add(e)
        }
        return false
    }
}
