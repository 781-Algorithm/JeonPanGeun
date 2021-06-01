
# 옥상 정원
import sys
input = sys.stdin.readline

n = int(input())
h = [int(input()) for _ in range(n)]

stack = []
cnt = 0

for i in range(n):
    while stack != [] and stack[-1] <= h[i]:
        stack.pop()

    stack.append(h[i])
    cnt += len(stack)-1

print(cnt)
