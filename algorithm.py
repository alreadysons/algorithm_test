def sol(N) :
    for i in range(1,N-1) :
        chk_list = [int(j)for j in str(i)]
        chk_sum = sum(chk_list) + i
        if chk_sum == N :
            return (print(i))
    return print(0)
        
N = int(input())
sol(N)
