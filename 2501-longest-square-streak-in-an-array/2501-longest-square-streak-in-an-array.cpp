class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        unordered_map<int, int> dp;
        int res = 0;
        sort(begin(nums), end(nums));
        for(auto i : nums){
            int root = sqrt(i);
            if(root * root == i)
		        dp[i] = 1 + dp[root];
		    else 
		        dp[i] = 1;
            res = max(res, dp[i]);
        }
        return res < 2 ? -1 : res;
    }
};