def solution(absolutes, signs):
    index = []
    answer = 0
    for i in range(len(absolutes)) :
        if signs[i] == True :
            index.append(absolutes[i])
        elif signs[i] == False :
            index.append(-1*absolutes[i])
    for i in range(len(index)) :
        answer += index[i]
    return answer
print(solution([4,7,12],[True,False,True]))