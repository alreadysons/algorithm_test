import sys
usr_input = int(sys.stdin.readline())
li = []
for i in range(usr_input):
    chk = sys.stdin.readline().rstrip().split()
    if len(chk) == 1:
        command = int(chk[0])
        if command == 2:
            print(li.pop() if li else -1)
        elif command == 3:
            print(len(li))
        elif command == 4:
            print(0 if li else 1)
        elif command == 5:
            print(li[-1] if li else -1)
    elif len(chk) == 2:
        li.append(int(chk[1]))
