# 로봇 청소기

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 1

def turn(d):
    d = (d+3) % 4
    return d

while True:

    # 현재 위치 청소
    if arr[x][y] == 0:
        arr[x][y] == -1 # 방문 처리
        cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        nd = turn(d)
        flag = False

        if (0 <= nx < n and \
                0 <= ny < m):
            if arr[nx][ny] == 0:
                cnt += 1
                arr[nx][ny] = -1 # 방문
                x, y = nx, ny
                flag = True
                break

    if not check:
        nx = x - dx
        ny = y - dy
        if (0 <= nx < n and \
                0 <= ny < m):
            if arr[nx][ny] == -1:
                x, y = nx, ny
            elif arr[nx][ny] == 0:
                print(cnt)
                break
    else:
        print(cnt)
        break