/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let prev = 0;
    for (let i=0; i<nums.length; i++) {
        nums[i] += prev;
        prev = nums[i]
    }
    return nums;
    
};