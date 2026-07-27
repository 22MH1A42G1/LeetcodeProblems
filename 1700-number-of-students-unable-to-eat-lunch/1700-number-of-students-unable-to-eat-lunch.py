class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stq = deque(students)
        swq = deque(sandwiches)
        c = 0
        n = len(students)
        while n:
            if stq[0] == swq[0]:
                stq.popleft()
                swq.popleft()
                n=len(stq)
            else:
                stq.append(stq[0])
                stq.popleft()
                n-=1
        return len(stq)