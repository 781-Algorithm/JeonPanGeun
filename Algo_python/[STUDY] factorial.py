# 재귀 함수로 팩토리얼 구하는 방법

def factorial_for(n):
    if n == 0 or n == 1:
        return 1

    answer = 1
    for i in range(1, n+1):
        answer = answer * i
    return answer

def factorial_recursion(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursion(n-1)


print(factorial_for(5))
print(factorial_recursion(5))