num = []
s = input()
a = int(s)
for i in range(len(s)):
    num.append(a % 10)
    a = a//10
slv = sorted(num, reverse=True)
print("".join(str(i) for i in slv))
