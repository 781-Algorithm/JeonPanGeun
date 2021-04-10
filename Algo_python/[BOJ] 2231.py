
N = int(input())

for i in range(0, N+1):
    temp = list(map(int, str(i)))

    if i + sum(temp) == N:
        print(i)
        break

    if N == i:
        print(0)