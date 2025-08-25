from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

def dfs(node,visited):
    if node not in visited:
        print(node,end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor,visited)


def bfs(start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node,end=' ')
            visited.add(node)
            queue.extend(graph[node])


print("DFS:")
dfs("A",set())

print("\nBFS:")
bfs('A')


