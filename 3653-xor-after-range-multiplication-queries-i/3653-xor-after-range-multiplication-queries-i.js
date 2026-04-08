/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number}
 */
var xorAfterQueries = function(nums, queries) {
    for(const [l,r,k,v] of queries){
        for (let i=l;i<r+1;i+=k){
            nums[i]=(nums[i]*v)%(1e9+7);
        }
    }
    // let result = 0;
    // for(let i=0;i<nums.length;i++){
    //     result^=nums[i];
    // }
    return nums.reduce((i,j)=>i^j,0);

};