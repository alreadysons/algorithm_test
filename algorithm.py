import math

def count_possible_positions(x1, y1, r1, x2, y2, r2):
    # 두 중점 사이의 거리 계산
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # 두 원이 일치하는 경우 (무한대의 좌표)
    if distance == 0 and r1 == r2:
        return -1
    
    # 두 원이 외접하거나 내접하는 경우 (한 개의 접점)
    if distance == r1 + r2 or distance == abs(r1 - r2):
        return 1
    
    # 두 원이 만나는 경우 (두 개의 접점)
    if abs(r1 - r2) < distance < r1 + r2:
        return 2
    
    # 그 외의 경우 (만날 수 없음)
    return 0

# 테스트 케이스 개수 입력
T = int(input())

for _ in range(T):
    # 테스트 케이스 입력
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    # 류재명이 있을 수 있는 좌표의 수 계산
    result = count_possible_positions(x1, y1, r1, x2, y2, r2)
    
    # 결과 출력
    print(result)
