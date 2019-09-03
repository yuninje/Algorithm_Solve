def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for r in range(len(answer)):
        for c in range(len(answer[0])):
            for a in range(len(arr2)):
                answer[r][c] += arr1[r][a] * arr2[a][c] 
    return answer