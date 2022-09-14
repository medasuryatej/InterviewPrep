class Solution {
    public int numSquares(int n) {
        // dp array
        int[] dp = new int[n+1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        
        // squares array
        int max_square_index = (int) Math.sqrt(n) + 1;
        int[] squares = new int[max_square_index];
        
        for (int i=0; i<max_square_index; i++) {
            squares[i] = i*i;
        }
        
        for (int i=1; i<=n; i++) {
            for (int s=1; s<max_square_index; s++) {
                if (i < squares[s] ) break;
                dp[i] = Math.min(dp[i], dp[i-squares[s]] + 1);
            }
        }
        
        return dp[n];
    }
}