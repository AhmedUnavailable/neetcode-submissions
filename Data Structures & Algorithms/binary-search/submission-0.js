class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let l = 0, r = nums.length -1;
        while (l<=r){
            let m = Math.floor((l+r)/2)
            console.log(m)
             
            if (nums[m] === target){
                return m
            }
            if (target > nums[m]){
                l = m +1
                
            }else {
                r = m -1
                
            }
        }
        return -1
    }
}
