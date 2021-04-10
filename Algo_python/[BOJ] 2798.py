

# 백준 2798 블랙잭


N, M = map(int, input().split())
card = list(map(int, input().split() ))
sum = []

for i in range(0, len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            tempSum = card[i] + card[j] + card[k]
            if tempSum > M:
                continue
            else:
                sum.append(tempSum)

print(max(sum))