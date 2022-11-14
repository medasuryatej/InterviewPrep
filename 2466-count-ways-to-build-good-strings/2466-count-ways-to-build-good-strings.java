class Solution {
    
    public int countGoodStrings(int low, int high, int zero, int one) {
        int result = 0;
        int[] dp = new int[high + 1];
        Arrays.fill(dp,-1);
        
        for (int i=low; i<=high; i++) {
            result = (result + dfs(zero, one, i, dp)) % 1000000007; 
            // System.out.println(result);
        }
        return result;
    }
    
    public int dfs(int zero, int one, int current, int dp[]) {
        if (current == 0) {
            // reached the target length
            return 1;
        }
        if (current < 0) {
            // reached outof bounds
            return 0;
        }
        if (dp[current] != -1) {
            return dp[current];
        }
        
        int addZeroZeroTimes = dfs(zero, one, current-zero, dp);
        int addOneOneTimes = dfs(zero, one, current-one, dp);
        
        dp[current] = (addZeroZeroTimes + addOneOneTimes)% 1000000007;
        
        return dp[current] % 1000000007;
            
    }
}