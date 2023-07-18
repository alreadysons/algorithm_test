a = []
for i in range(5) :
    b = int(input())
    a.append(b)
c = sorted(a)
avg = 0
for i in range(len(c)) :
    avg +=c[i]
print(avg//5)
print(c[2])