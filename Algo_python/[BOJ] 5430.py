import sys
input = lambda : sys.stdin.readline().strip()
from collections import deque

# input
t = int(input())

for _ in range(t):
    cmd = input()
    n = int(input())
    arr = input()[1:-1].split(',')
    cmd = cmd.replace('RR', '')
    de = deque()

    for i in arr:
        if i != '':
            de.append(i)

    cnt = 0
    flag = 0

    for i in cmd:
        if i == "R":
            cnt += 1

        elif i == "D":
            if len(de) == 0:

                flag = 1 # 에러일 때.
                break

            else:
                if cnt % 2 == 0:
                    de.popleft()
                else:
                    de.pop()


    if flag == 1:
            print("error")
    else:
        if cnt % 2 == 1:
            de.reverse()

        print("[", end='')
        for i in range(len(de)):
            if i == len(de) - 1:
                print(de[i], end='')
            else:
                print(str(de[i]) + ",", end='')
        print("]")









