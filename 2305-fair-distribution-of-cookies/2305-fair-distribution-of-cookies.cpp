class Solution {
public:
    int ans = INT_MAX;
    void solve(vector<int>& cookies, vector<int>& bag, int i, int k) {
        if (i >= cookies.size()) {
            int tmp = 0;
            for (int ele: bag) tmp = max(tmp, ele);
            ans = min(ans, tmp);
            return;
        }
        
        for (int j=0; j<k; j++) {
            bag[j] += cookies[i];
            solve(cookies, bag, i+1, k);
            bag[j] -= cookies[i];
            
        }
        return ;
    }
    
    int distributeCookies(vector<int>& cookies, int k) {
        vector<int> bag(k,0);
        solve(cookies, bag, 0, k);
        return ans;
    }
};