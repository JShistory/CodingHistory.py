n = int(input())
target = 1
coins = list(map(int, input().split(" ")))
coins.sort()

for i in coins:
    if target < i:
        break
    else:
        target +=i
print(target)
