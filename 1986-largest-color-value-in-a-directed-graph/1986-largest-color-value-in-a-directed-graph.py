class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        def dfs(source, graph, topo_ordering):
            if in_stack[source]:
                return True
            if visited[source]:
                return False
            visited[source] = True
            in_stack[source] = True
            for i in graph[source]:
                if dfs(i, graph, topo_ordering):
                    return True
            in_stack[source] = False
            topo_ordering.append(source)
            return False 

        n = len(colors)
        visited = [False for _ in range(n)]
        in_stack = [False for _ in range(n)]
        graph = [[] for _ in range(n)]
        for start, end in edges:
            graph[start].append(end)
        topo_ordering = []
        for i in range(n):
            if not visited[i]:
                if dfs(i, graph, topo_ordering):
                    return -1
        col_dict = {i:{} for i in range(n)}
        ans = 1
        for i in topo_ordering:
            if not graph[i]:
                col_dict[i][colors[i]] = 1
            else:
                for j in graph[i]:
                    for entry in col_dict[j]:
                        if entry not in col_dict[i]:
                            col_dict[i][entry] = col_dict[j][entry]
                        else:
                            col_dict[i][entry] = max(col_dict[i][entry], col_dict[j][entry])
                if colors[i] in col_dict[i]:
                    col_dict[i][colors[i]] += 1
                    if col_dict[i][colors[i]] > ans:
                        ans = col_dict[i][colors[i]]
                else:
                    col_dict[i][colors[i]] = 1
        return ans