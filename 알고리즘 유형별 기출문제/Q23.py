n = int(input())
student = []
for i in range(n):
    [name, kor, eng, math] = map(str, input().split())
    student.append([name,int(kor),int(eng),int(math)])

student = sorted(student, key=lambda x : (-x[1],x[2],-x[3],x[0]))
for i in student:
    print(i[0])


