s = input()

sum = int(s[0])

for i in s:
    number = int(i)
    if number<=1 or sum <=1:
        sum +=number

    else:
        sum*=number

print(sum)