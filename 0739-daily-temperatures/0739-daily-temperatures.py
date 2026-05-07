class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer=[0]*len(temperatures)#[0,0,0,0,0,0,0,0]
        s=[]
        for i in range(len(temperatures)):
            while s and temperatures[i] > temperatures[s[-1]]:
                a=s.pop()
                answer[a]=i-a
            s.append(i)
        return answer