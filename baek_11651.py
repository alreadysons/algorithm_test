def main():
    N = int(input())
    points = []
    x_points = []
    # Parsing input points
    for _ in range(N):
        x,y = map(int,input().split())
        if x==0 :
            x_points.append((x,y))
        else :
            points.append((x,y))
    
    # Sorting points by x, then by y if x is the same
    points.sort()
    x_points.sort()
    
    # Printing sorted points
    for x,y in points :
        print(x,y)
    for x,y in x_points:
        print(x,y)

if __name__ == "__main__":
    main()
