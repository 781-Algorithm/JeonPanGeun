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




while True:
    sentence = input().rstrip()
    stack = Stack()
    flag = False

    for c in sentence:
        if c == '(' or c == '[':
            stack.push(c)
        elif c == ')':
            if stack.size() != 0 and stack.peek() == '(':
                stack.pop()
            else:
                print('no')
                flag = True
                break

        elif c == ']':
            if stack.size() != 0 and stack.peek() == '[':
                stack.pop()
            else:
                print('no')
                flag = True
                break
    if sentence == '.':
        break

    if stack.size() != 0 and flag == False:
        print('no')

    elif stack.size() == 0 and flag == False:
        print('yes')