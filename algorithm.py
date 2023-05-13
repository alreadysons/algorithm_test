def solution():
    N = int(input())
    S = input()
    if N<1 and N>100 :
        return False
    elif S not in "T" :
        return False
    chk_A = 0
    chk_T = 0
    for i in range(N) :
        if S[i] == "T" :
            chk_T +=1
        elif S[i] == "A" :
            chk_A +=1
    if chk_A>chk_T :
        return print("A")
    elif chk_A<chk_T or chk_T == chk_A :
        return print("T")
solution()