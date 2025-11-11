class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0,0):0}
        for s in strs:
            ones = s.count('1')
            zeroes = s.count('0')
            newdp = {}
            for (pz,po), val in dp.items():
                nz,no = pz+zeroes, po+ones
                if nz<=m and no <= n:
                    if (nz,no) not in dp or dp[(nz,no)]<val+1:
                        newdp[(nz,no)]=val+1
            dp.update(newdp)
        return max(dp.values())