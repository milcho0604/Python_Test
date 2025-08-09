import sys
# n = int(input())

# 시간 초과로 입력을 빠르게 받기 위해 sys를 사용
input = sys.stdin.readline
n = int(input().strip())
arr = [int(input()) for _ in range(n)]

# 배열 오름차순 정렬
arr.sort()
# 내림차순 정렬을 하고 싶다면 -> arr.sort(reverse=True)

for i in range(len(arr)):
    print(arr[i])