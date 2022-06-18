/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    let prev = 0;
    for (let i=1; i <nums.length; i++) {
        if (i > 1) {
            nums[i] = Math.max(nums[i] + nums[i-2], nums[i-1]);
        } else {
            nums[i] = Math.max(nums[i] + 0, nums[i-1]);   
        }  
    }
    return nums[nums.length - 1];
};