#재귀로 구현한 이진탐색
def binary_search(array,target,start,end):
    if start >= end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

array = list(map(int, input().split()))
array.sort()
target = int(input())

result= binary_search(array,target,0,len(array)-1)
if result == None:
    print("찾는 값이 없습니다.")
else:
    print(result+1)


