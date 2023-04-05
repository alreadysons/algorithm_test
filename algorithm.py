def solution(x):
    answer = True
    lili = []
    arr = 0
    z = x
    while z != 0 :
        lili.append(z%10)
        z = z//10
    for i in range(len(lili)) :
        arr += lili[i]
    if x%arr == 0 :
        answer = True
    elif x%arr != 0 :
        answer = False
    return answer
print(solution(11))