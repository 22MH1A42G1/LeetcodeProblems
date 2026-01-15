class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        hm, vm = 1, 1
        hc, vc = 1, 1
        for i in range(1, len(hBars)):
            if hBars[i]==hBars[i-1]+1:
                hc+=1
            else:
                hc=1
            hm=max(hm,hc)
        for i in range(1, len(vBars)):
            if vBars[i]==vBars[i-1]+1:
                vc+=1
            else:
                vc=1
            vm=max(vm,vc)
        s=min(hm,vm)+1
        return s*s