a = int(input())
c = []
for i in range(a) :
    b = int(input())
    c.append(b)
cc = sorted(c)
for i in range(len(cc)) :
    print(cc[i])