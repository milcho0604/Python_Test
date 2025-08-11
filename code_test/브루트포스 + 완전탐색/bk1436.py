n = int(input())

m = 666
count = 0

while True:
    if '666' in str(m):
        count += 1
    
    # count가 입력한 n과 같다면 stop
    if count == n:
        break
    # m을 하나씩 올린다. 
    m +=1 

print(m)
