n = int(input())

result = []

for _ in range(n):
    result.append(input())

result.sort()

for i in range(len(result)):
    print(result[i])
    
    # 만약 한 줄로 1 2 3 4 5와 같이 출력하고 싶다면 아래 end 추가
    # print(result[i], end=' ')