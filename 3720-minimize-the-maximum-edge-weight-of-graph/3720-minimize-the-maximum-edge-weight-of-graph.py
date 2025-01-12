class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        edges.sort(key=lambda x: x[2])
        weights = sorted(set(w for _, _, w in edges))

        def is_valid_graph(max_weight):
            graph = defaultdict(list)
            reverse_graph = defaultdict(list)

            for u, v, w in edges:
                if w <= max_weight:
                    graph[u].append(v)
                    reverse_graph[v].append(u)

            visited = [False] * n
            queue = deque([0])
            visited[0] = True

            while queue:
                node = queue.popleft()
                for neighbor in reverse_graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

            if not all(visited):
                return False

            for node in range(n):
                if len(graph[node]) > threshold:
                    min_heap = []
                    for neighbor in graph[node]:
                        heapq.heappush(min_heap, neighbor)
                        if len(min_heap) > threshold:
                            heapq.heappop(min_heap)
                    graph[node] = list(min_heap)

            return True

        left, right = 0, len(weights) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if is_valid_graph(weights[mid]):
                result = weights[mid]
                right = mid - 1
            else:
                left = mid + 1

        return result