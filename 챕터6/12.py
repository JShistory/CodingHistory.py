n,m = map(int, input().split(" "))
list1 = []
list2 = []

list1 = list(map(int, input().split(" ")))
list2 = list(map(int, input().split(" ")))
print(list1,list2)
list1.sort()
list2.sort(reverse=True)
for i in range(m):
    if list1[i] < list2[i]:
        list1[i],list2[i] = list2[i],list1[i]
    else:
        break
print(sum(list1))