import sys
input = sys.stdin.readline

n = int(input())
result = 0

# 자릿수 * 9
ranges = n - (9 * int(len(str(n))))

for i in range(ranges, n):
    num = i
    sum = 0
    print('첫 번째: ', num)

    # /10 방식으로 각 자릿수 합 구하기
    while num > 0:
        print('i: ', i)
        sum += num % 10  # 마지막 자리 더하기
        print('두 번째: ',sum)
        num //= 10  # 마지막 자리 제거
        print('세 번째: ',num)

    total = i + sum  # 분해합

    if total == n:
        result = i
        break

print(result)