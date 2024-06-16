import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n=int(input())
board=[]
for _ in range(n):
    board.append(list(map(int, input().split())))
d=[[-1 for col in range(n)] for row in range(n)]

def go(x, y):
	if(x < 0 or x >= n or y < 0 or y >= n):
		return 1e9
	
	global d
	if(x == n - 1 and y == n - 1):
		d[x][y] = 0
		return d[x][y]
	
	if (d[x][y] == -1): 
		d[x][y]=0
	else:
		return d[x][y]
	
	tmp = 1e9
	if(x + 1 < n):
		cl = board[x + 1][y] - board[x][y]
		if(cl <= 0): cl = 0
		tmp = min(tmp, go(x + 1, y) + cl)
	
	if(y + 1 < n):
		cl = board[x][y + 1] - board[x][y]
		if(cl <= 0): cl = 0
		tmp = min(tmp, go(x, y + 1) + cl)
	
	d[x][y] = tmp;
	return d[x][y]

res = go(0, 0)
print(res)