class Solution {
public:
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        // dp array of 3 dimensions
        // [rows][cols][the various mod values possible]
        // [rows][cols][ (kk + grid[i][j]) % k ]
        int n = grid.size(), m = grid[0].size();
        int dp[n][m][k];
        
        memset(dp, 0, sizeof(dp));
        dp[0][0][grid[0][0]%k] = 1;
        for (int i=0; i < n; i++) {
            for (int j=0; j<m; j++) {
                for (int l=0; l <k; l++) {
                    if (j > 0) {
                        // from 0 to k-1 determine if that mod is possible by adding values from neighbours i-1,j and i and j-1
                        dp[i][j][(l + grid[i][j]) % k] += dp[i][j-1][l] % 1000000007;
                    } 
                    if (i > 0) {
                        dp[i][j][(l + grid[i][j]) % k] += dp[i-1][j][l] % 1000000007;
                    }
                }
            }
        }
        return dp[n-1][m-1][0] % 1000000007;
    }
};