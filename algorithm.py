a=int(input())
s=[]
input_com = []
for i in range(a) :
    input_com = [x for x in input().split()]
    if input_com[0] == "push" :
        s.append(int(input_com[1]))
    elif input_com[0] == "top" :
        if len(s) !=0 :
            print(s[-1])
        else : print(-1)    
    elif input_com[0] == "size" :
        print(len(s))
    elif input_com[0] == "pop" :
        if len(s) !=0 :
            print(s.pop())
        else : print(-1)
    elif input_com[0] == "empty" :
        if len(s) == 0 :
            print(1)
        else :
            print(0)
