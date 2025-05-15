class Solution {
    public static boolean isVowel(char c){
        String vowels = "aeiouAEIOU";
        return vowels.contains(""+c);
    }
    public String reverseVowels(String s) {
        char[] A = s.toCharArray();
        int i=0;
        int j=A.length-1;
        while (i<j){
            if (isVowel(A[i]) && isVowel(A[j])){
                char ch =A[i];
                A[i]=A[j];
                A[j]=ch;
                i++;
                j--;
            }
            else if(isVowel(A[i])){
                j--;
            }
            else if(isVowel(A[j])){
                i++;
            }
            else{
                i++;
                j--;
            }
        }
        return new String(A);
    }
}