class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int numArrays = 0;
        int[] remFreq = new int[k];
        remFreq[0] = 1;
        int cummSum = 0;
        int rem = 0;
        for (int i=0; i<nums.length; i++) {
            cummSum += nums[i];
            rem = cummSum % k;
            if (rem < 0) {
                rem += k;
            }
            numArrays += remFreq[rem];
            remFreq[rem]++;
        }
        return numArrays;
    }
}