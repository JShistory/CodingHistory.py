n, m = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
start = 0
end = max(a)
result = 0
while start <= end:
    h = 0
    mid = (start + end) // 2
    for i in a: #떡을 하나씩 조사해서
        if i > mid: #만약 떡의 길이가 mid보다 길다면 즉 짜를 수 있다면
            h += i-mid #h에다가 잘린값을 저장한다.
    if h <m:  #근데 만약에 h이 n의값보다 작다면 즉 떡을 더 많이 짤라야 한다면
        end = mid - 1
    else:
        result = mid
        start = mid + 1


print(result)
