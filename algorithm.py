a,b = map(int,input().split())
a_list = sorted(map(int,input().split()))
ab = b

for i in range(len(a_list)) :
    chk = 0
    for j in range(len(a_list)) :
        for k in range(len(a_list)) :
            if i==j or j==k or i==k :
                continue
            chk = a_list[i]+a_list[j]+a_list[k]
            if chk > b :
                continue
            num = b-chk
            ab = min(num,ab)

print(b-ab)
