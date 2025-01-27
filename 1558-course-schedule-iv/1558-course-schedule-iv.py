class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for p in prerequisites:
            adj[p[0]].append(p[1])
            indegree[p[1]] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        mp = defaultdict(set)
        while q:
            curr = q.popleft()
            for next_course in adj[curr]:
                mp[next_course].add(curr)
                mp[next_course].update(mp[curr])
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)
        
        return [q[0] in mp[q[1]] for q in queries]