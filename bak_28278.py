usr_input = int(input())
li = []
for i in range(usr_input):
    chk = input().split()
    if len(chk) == 1:
        if int(chk[0]) == 2:
            if len(li) != 0:
                print(li.pop())
            else:
                print(-1)
        elif int(chk[0]) == 3:
            print(len(li))
        elif int(chk[0]) == 4:
            if len(li) != 0:
                print(0)
            else:
                print(1)
        elif int(chk[0]) == 5:
            if len(li) != 0:
                print(li[-1])
            else:
                print(-1)
    elif len(chk) == 2:
        li.append(int(chk[1]))
