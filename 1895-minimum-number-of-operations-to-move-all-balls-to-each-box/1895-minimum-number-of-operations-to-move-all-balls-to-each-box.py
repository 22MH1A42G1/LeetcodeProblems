class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)#(0,0,0)
        for i in range(len(boxes)):   #range(3):->
            if boxes[i] == "1":#b(0)-$,b(1)-$,b(2)-#
                for j in range(len(boxes)):#range(3):->
                    ans[j] += abs(j - i)#ans=((0+1+0),(1+0+0),(2+1+0))
        return ans