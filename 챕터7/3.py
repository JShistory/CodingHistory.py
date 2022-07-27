#반복문으로 구현한 이진 탐색
def binary_search(array,target,start,end):

    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            mid = end - 1
    return None

array = list(map(int, input().split()))
array.sort()
target = int(input())

result= binary_search(array,target,0,len(array)-1)
if result == None:
    print("찾는 값이 없습니다.")
else:
    print(result+1)

