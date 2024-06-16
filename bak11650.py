def main():
    N = int(input())
    points = []
    
    # Parsing input points
    for _ in range(N):
        x,y = map(int(input().split()))
        points.append((x,y))
    
    # Sorting points by x, then by y if x is the same
    points.sort()
    
    # Printing sorted points
    for x,y in points :
        print(x,y)

if __name__ == "__main__":
    main()
