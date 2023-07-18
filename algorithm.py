a=int(input())
s = []
for i in range(a) :
    b = int(input())
    s.append(b)
c = sorted(s)
for i in range(len(s)) :
    print(c[i])
