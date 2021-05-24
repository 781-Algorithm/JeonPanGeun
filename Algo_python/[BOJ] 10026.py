# 적록색약
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):

    q.append([x, y])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx and nx < n and \
                0 <= ny and ny < n:
                if arr[nx][ny] == arr[x][y] and visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1


n = int(input())
arr = [list(map(str, input())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
rgVisited = [[0 for _ in range(n)] for _ in range(n)]
q = deque()

cnt = 0 # 일반구역 수
rgCnt = 0 # 적록색약 구역 수


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1

visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            rgCnt += 1

print(cnt, rgCnt)


