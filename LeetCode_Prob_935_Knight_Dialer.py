class Solution:
    def knightDialer(self, n: int) -> int:
        """
        The knight can jump from number x to below mentioned possible positions
        """
        knightMapper = {
            0: [4,6],
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [3,9,0],
            5: [],
            6: [1,7,0],
            7: [6,2],
            8: [3,1],
            9: [4,2]
        }
        # initialzie dp to zero
        dp = [[0 for i in range(10)] for j in range(n+1)]
        # for one move we can be on any of the 10 numbers in number pad
        dp[1] = [1 for i in range(10)]
        #
        mod = 10**9 + 7
        
        for num_idx in range(2, n+1):
            for i in range(10):
                # for any  given step, we can tarverse to all other steps in the mapper
                # meaning to reach number 0 on step 3, we must be at number 4 or 6 in step 2 (so both those results summate to  current step)
                dp[num_idx][i] = sum([dp[num_idx-1][j] for j in knightMapper[i]]) % mod
        return sum(dp[n]) % mod
