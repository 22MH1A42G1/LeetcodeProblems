class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n=s.length();
        int m=0;
        Set<Character>charSet=new HashSet<>();
        int l=0;
        for(int r=0;r<n;r++){
            if(!charSet.contains(s.charAt(r))){
                charSet.add(s.charAt(r));
                m=Math.max(m,r-l+1);
            }else{
                while(charSet.contains(s.charAt(r))){
                    charSet.remove(s.charAt(l));
                    l++;
                }
                charSet.add(s.charAt(r));
            }
        }
        return m;
    }
}