class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();
        // vector<int> v1,v2;
        set<int> r;
        set<int> c;
        
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                if(matrix[i][j] == 0)
                {
                    r.insert(i);
                    c.insert(j);
                }
            }
        }
        
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<m; j++)
            {
                if(r.count(i) or c.count(j))
                    matrix[i][j] = 0;
            }
        }
       
    }
};