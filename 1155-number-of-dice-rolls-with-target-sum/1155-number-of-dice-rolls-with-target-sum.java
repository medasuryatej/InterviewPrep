class Solution {
    
    final int MOD = 1000000007;
        
    public int numRollsToTarget(int n, int k, int target) {
        Integer[][] dp = new Integer[n+1][target+1];
        int result = numWaysToRoll(dp, 0, n, 0, target, k);
        return result % MOD;
    }
    
    public int numWaysToRoll(Integer[][] dp, int index, int n, int cursum, int target, int k) {
        // reached end
        if (index == n) {
            // check if cursum == target
            return cursum == target? 1 : 0;
        }
        
        // check if this combo is seen in dp
        if (dp[index][cursum] != null) {
            return dp[index][cursum];
        }
        
        int ways = 0;
        int minDieFaces = Math.min(k, target-cursum);
        
        // checking for every possible k value
        for (int i=1; i<=minDieFaces; i++) {
            ways = (ways + numWaysToRoll(dp, index+1, n, cursum + i, target, k)) % MOD;
        }
        
        dp[index][cursum] = ways;
        
        return dp[index][cursum] % MOD;
    }
}