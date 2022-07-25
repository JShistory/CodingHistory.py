n = int(input())
n = str(n)
nsize = int(len(n)/2)
sum1 = 0
sum2 = 0
for i in range(nsize):
    sum1 += int(n[i])
for i in range(nsize,len(n)):
    sum2 += int(n[i])
if sum1 == 6 and sum2 == 6:
    print("LUCKY")
else:
    print("READY")