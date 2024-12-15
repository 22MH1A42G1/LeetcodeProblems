class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        m = events[0][1]
        b = events[0][0]
        for i in range(1,len(events)):
            t = events[i][1] - events[i-1][1]
            if t > m or (t==m and events[i][0] < b):
                m = t
                b = events[i][0]
        return b