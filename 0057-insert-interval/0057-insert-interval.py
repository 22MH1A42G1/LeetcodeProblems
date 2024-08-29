class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)

        answer = [newInterval]

        

        for idx in range(n):

            start = max(intervals[idx][0],answer[-1][0])

            end = min(intervals[idx][1],answer[-1][1])

            if start <= end:

                answer[-1][0] = min(intervals[idx][0],answer[-1][0])

                answer[-1][1] = max(intervals[idx][1],answer[-1][1])

            elif end < newInterval[1]:

                answer.pop()

                answer.append(intervals[idx])

                answer.append(newInterval)

            else:

                answer.append(intervals[idx])

        return answer