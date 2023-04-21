def solution(n, m, section):
    answer = 0
    section.sort()
    section_lenght = len(section)
    idx = 0
    while idx <section_lenght:
        answer +=1
        start = section[idx]
        end = start + m - 1
        while idx <section_lenght and section[idx] <= end :
            idx +=1
    return answer
print(solution(4,1,[1,2,3,4]))