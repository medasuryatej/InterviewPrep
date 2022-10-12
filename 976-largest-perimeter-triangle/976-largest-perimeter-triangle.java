class Solution {
    public int largestPerimeter(int[] nums) {
        // sort the parameters
        // start checking from the end
        // if a + b > c then the largest triangle can be formed
        Arrays.sort(nums);
        for (int i = nums.length - 3; i >= 0; i--) {
            if (nums[i] + nums[i+1] > nums[i+2]) {
                return nums[i] + nums[i+1] + nums[i+2];
            }
        }
        return 0;
    }
}