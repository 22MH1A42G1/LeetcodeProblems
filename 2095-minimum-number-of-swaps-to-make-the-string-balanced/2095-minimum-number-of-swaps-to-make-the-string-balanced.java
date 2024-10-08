class Solution {
    public int minSwaps(String s) {
    int open = 0;
    int mismatch = 0;     
    for(int i=0; i<s.length(); i++)
    {
      char ch = s.charAt(i);
      if(ch=='[')
      {
        open++;
      }
        else{
            if(open>0)
            {
              open--; 
            }
            else
                mismatch++; 
        }
    }
     int n = open + mismatch;
     int ans = 0; 
     while(n>0)
     {
      ans++;
         n = n-4; 
     }
        return ans; 
    }
}