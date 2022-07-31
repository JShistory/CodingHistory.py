s = input()
answer = len(s)
steps = []


for step in range(1,len(s) // 2 + 1):
    steps = s[0:step]
    com = ""
    count = 1

    for n_step in range(step,len(s),step):
        if steps == s[n_step:n_step+step]:
            count +=1
        else:
            com += str(count)+steps if count>=2 else steps
            count = 1
    com += str(count) + steps if count >=2 else steps

    answer = min(answer, len(com))

print(answer)
