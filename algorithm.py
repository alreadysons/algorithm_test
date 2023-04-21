def solution(common):
    answer = 0
    diff = common[1] - common[0]
    ratio = common[1] // common[0] if common[0] != 0 else None

    is_arithmetic = all(common[i+1] - common[i] == diff for i in range(len(common) - 1))
    is_geometric = all(common[i+1] // common[i] == ratio for i in range(len(common) - 1)) if ratio is not None and all(c != 0 for c in common[:-1]) else False

    if is_arithmetic:
        answer = common[-1] + diff
    elif is_geometric:
        answer = common[-1] * ratio
        
    return answer
