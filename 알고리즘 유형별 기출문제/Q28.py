from bisect import bisect_right,bisect_left
n = int(input())
data = list(map(int, input().split()))
index = 0
for i in range(len(data)):
    left = bisect_left(data,data[i])
    right = bisect_right(data,data[i])
    if bisect_left(data,data[i])==data[i]:

        index = data[i]
        break
if index == 0:
    print(-1)
else:
    print(index)


