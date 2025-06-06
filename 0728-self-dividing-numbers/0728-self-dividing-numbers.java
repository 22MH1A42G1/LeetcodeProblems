import java.util.List;
import java.util.ArrayList;
class Solution {
    public boolean isSD(int num){
        int temp = num;
        while (num > 0) {
            int rem = num % 10;
            if (rem == 0 || (temp % rem) != 0) {
                return false;
            }
            num /= 10;
        }
        return true;
    }
    public List<Integer> selfDividingNumbers(int left, int right) {
        ArrayList<Integer> ans = new ArrayList<>();
        for(int i=left; i<=right;i++){
            if(isSD(i)){
                ans.add(i);
            }
        }
        return ans;
    }
}