
### 괄호
# 입력
# 입력 데이터는 표준 입력을 사용한다.
# 입력은 T개의 테스트 데이터로 주어진다.
# 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.
# 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다.
# 하나의 괄호 문자열의 길이는 2 이상 50 이하이다.

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

for _ in range(n):
    bracket = input()
    stack = Stack()
    flag = False

    for c in bracket:
        if c == '(':
            stack.push(c)
        elif c == ')':
            if stack.size() != 0:
                stack.pop()
            else:
                print("NO")
                flag = True
                break

    if stack.size() != 0 and flag == False:
        print("NO")
    elif stack.size() == 0 and flag == False:
        print("YES")