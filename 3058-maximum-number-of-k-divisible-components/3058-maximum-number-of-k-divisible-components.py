class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], vals: List[int], k: int) -> int:
        from collections import deque, defaultdict
        
        if n < 2:
            return 1
        
        graph = defaultdict(list)
        degree = [0] * n
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1
        
        node_vals = vals[:]
        leaf_q = deque([i for i in range(n) if degree[i] == 1])
        comp_cnt = 0
        
        while leaf_q:
            curr = leaf_q.popleft()
            degree[curr] -= 1
            carry = 0
            
            if node_vals[curr] % k == 0:
                comp_cnt += 1
            else:
                carry = node_vals[curr]
            
            for nbr in graph[curr]:
                if degree[nbr] == 0:
                    continue
                degree[nbr] -= 1
                node_vals[nbr] += carry
                if degree[nbr] == 1:
                    leaf_q.append(nbr)
        
        return comp_cnt