from bisect import bisect_left, bisect_right



n,target = map(int ,input().split())
data = list(map(int, input().split()))
if target not in data:
    print(-1)
elif bisect_right(data,target) > bisect_left(data,target):
    print(bisect_right(data,target)-bisect_left(data,target))
else:
    print(bisect_left(data, target) - bisect_right(data, target))


