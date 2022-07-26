n = int(input())
groups = list(map(int, input().split(" ")))
groups.sort()
count = 0
result = 0
for i in groups:
    count +=1
    if i == count:
        result +=1
        count=0
print(result)



