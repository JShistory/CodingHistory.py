def binary_search(array, target, start, end):
    while start<=end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid +1
        else:
            end = mid - 1
    return None
n = int(input())
a = list(map(int ,input().split(" ")))
a.sort()
m = int(input())
b = list(map(int, input().split(" ")))
for find in b:
    result = binary_search(a,find,0,n-1)
    if result != None:
        print("yes")
    else:
        print("no")
