
# 백준 10773 제로

# 첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)
#
# 이후 K개의 줄에 정수가 1개씩 주어진다.
# 정수는 0에서 1,000,000 사이의 값을 가지며,
# 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
#
# 정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

class Stack:
    def __init__(self):
        self.top = []

    def push(self, item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            print("Stack underflow")
            exit()

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            print("underflow")
            exit()

    def isEmpty(self):
        return len(self.top) == 0

    def size(self):
        return len(self.top)


n = int(input())
stack = []

for _ in range(n):
    money = int(input())

    if money != 0:
        stack.append(money)
    elif money == 0:
        stack.pop(-1)

print(sum(stack))