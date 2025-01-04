class Solution {
public:
    int countPalindromicSubsequence(string s) {
        int ans = 0;
        int n = s.length();
        
        unordered_map<char, pair<int, int>> M;
        
        for (int i = 0; i < n; i++) {
            if (M.find(s[i]) == M.end()) {
                M[s[i]].first = i;
            }
            M[s[i]].second = i;
        }
        
        for (auto& [ch, positions] : M) {
            int left = positions.first;
            int right = positions.second;
            
            if (right - left <= 1) continue;  // No valid subsequences in this range
            
            unordered_set<char> uniqueChars;
            for (int i = left + 1; i < right; i++) {
                uniqueChars.insert(s[i]);
            }
            
            ans += uniqueChars.size();  // Count the unique characters between first and last occurrence
        }
        
        return ans;
    }
};