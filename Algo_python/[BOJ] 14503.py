# 로봇 청소기

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn(d):
    d = (d+3) % 4
    return d

def clear(r, c, d):
    result = 1
    x, y = r, c

    while(True):

        # 현재 위치 청소
        if arr[x][y] == 0:
            arr[x][y] == -1
            result += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = turn(d)

            if (0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0):
                arr[nx][ny] == -1
                result += 1
                x = nx
                y = ny
                d = nd
                break

        # 반대 방향 바라보기
        nd = (d + 2) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]

        if arr[nx][ny] == 1:
            return
        else:
            clear(nx, ny, d)

    return result



n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

res = clear(r, c, d)

print(res)