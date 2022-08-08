def solution(N,stages):
    answer = []
    dict ={}
    people = len(stages)
    for i in range(1,N+1):
        if people != 0:
            dict[i] = stages.count(i)/people
            people -=stages.count(i)
        else:
            dict[i] = 0
    stages_list = sorted(dict.items(), key = lambda x : x[1], reverse= True)

    for i in stages_list:
        answer.append(i[0])
    return answer

N = 5
stages = [2,1,2,6,2,4,3,3]
print(solution(N,stages))