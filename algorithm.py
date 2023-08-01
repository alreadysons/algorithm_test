import sys
from collections import deque

a = int(input())
s = deque()
output = []

for i in range(a):
    input_com = input().split()
    if input_com[0] == "push":
        s.append(int(input_com[1]))
    elif input_com[0] == "top":
        output.append(str(s[-1]) if s else "-1")
    elif input_com[0] == "size":
        output.append(str(len(s)))
    elif input_com[0] == "pop":
        output.append(str(s.pop()) if s else "-1")
    elif input_com[0] == "empty":
        output.append("0" if s else "1")

# 결과 문자열을 한 번에 출력
sys.stdout.write("\n".join(output))
