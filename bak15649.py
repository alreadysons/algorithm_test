def backtrack(n, m, path, visited):
    if len(path) == m:
        print(" ".join(map(str, path)))
        return
    
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            path.append(i)
            backtrack(n, m, path, visited)
            path.pop()
            visited[i] = False

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    visited = [False] * (N + 1)
    backtrack(N, M, [], visited)

if __name__ == "__main__":
    main()
