
def fibo_count(n):
    zero = [1, 0]
    one = [0, 1]

    for i in range(2, n+1):
        zero.append(zero[i-1] + zero[i-2])
        one.append(one[i-1] + one[i-2])

    print(zero[n], one[n])

i = int(input())

for _ in range(i):
    n = int(input())
    fibo_count(n)
