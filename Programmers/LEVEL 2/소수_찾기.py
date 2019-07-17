num_list = []
def solution(numbers):
    answer = 0
    num = []
    # 숫자 조각 분리
    for i in numbers:
        num.append(i)
    # 숫자 조합 만들기
    bool_list = [False for _ in range(0,len(num))]
    for i in range(0,len(num)):
        make_num(num, bool_list.copy(), "",i)
    
    #소수 확인
    for num in num_list:
        if num != 0 and num != 1:
            answer += 1
            for i in range(2,num):
                if num % i == 0:
                    answer -= 1
                    break
    return answer


def make_num(num, bool_list, str_ ,add_num_index):
    bool_list[add_num_index] = True
    str_ += num[add_num_index]
    if not int(str_) in num_list:
        num_list.append(int(str_))
    for i in range(0, len(bool_list)):
        if not bool_list[i]:
            make_num(num, bool_list.copy(), str_.encode().decode(), i)