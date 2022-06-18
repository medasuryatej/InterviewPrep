/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.length < 4) {
        return Math.max(...nums);
    }
    let robbedFirstHouse = nums.slice(0,-1);
    // console.log(robbedFirstHouse);
    let robbedLastHouse = nums.slice(1,);
    // console.log(robbedLastHouse);
    return Math.max(HouseRobber(robbedFirstHouse), HouseRobber(robbedLastHouse));
};

function HouseRobber(nums) {
    for (let i=1; i<nums.length; i++) {
        if (i>1) {
            nums[i] = Math.max(nums[i] + nums[i-2], nums[i-1]);
        } else {
            nums[i] = Math.max(nums[i], nums[i-1]);
        }
    }
    // console.log(nums[nums.length -1]);
    return nums[nums.length -1];
}