

# DFS 재귀
def recursive_dfs(v, discovered=[]):
    discovered.append(v)

    for w in gragh[v]:
        if not w in discovered:
            discovered = recursive_dfs(w, discovered)

    return discovered


# DFS 스택을 이용한 반복
def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]

    while stack:
        v = stack.pop()

        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)

    return discovered

# BFS 큐르 이용한 반복
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]

    while queue:
        v = queue.pop(0)

        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)

    return discovered