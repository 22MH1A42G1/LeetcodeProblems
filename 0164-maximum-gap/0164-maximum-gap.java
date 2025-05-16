class Solution {
    public int maximumGap(int[] nums) {
        Arrays.sort(nums);
        int maxgap=0;
        for(int i=0;i<nums.length-1;i++){
            int gap = nums[i+1]-nums[i];
            if(gap>maxgap) maxgap = gap;
        }
        return maxgap;
    }
}