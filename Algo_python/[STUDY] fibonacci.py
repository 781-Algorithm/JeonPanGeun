# 피보나치 수열
# 메모제이션 : 자꾸 반복되지만 그 결과값은 변하지 않는 작은 문제들의 결과값을 저장하는 것

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

dic = {}

def fibonacci2(n):
    if n in dic:
        return dic[n]

    if n == 0:
        dic[0] = 0
        return 0
    elif n == 1:
        dic[1] = 1
        return 1
    else:
        dic[n] = fibonacci2(n-1) + fibonacci2(n-2)
        return dic[n]

print(fibonacci(10))
print(fibonacci2(10))