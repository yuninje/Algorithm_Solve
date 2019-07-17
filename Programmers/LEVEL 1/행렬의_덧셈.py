def solution(arr1, arr2):
    answer = []
    answer_ = []
    for i in range(0,len(arr1)):
        answer_ = []
        for j in range(0,len(arr1[i])):
            answer_.append(arr1[i][j] + arr2[i][j])
        answer.append(answer_)
    return answer