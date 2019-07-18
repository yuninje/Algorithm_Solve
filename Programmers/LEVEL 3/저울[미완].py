def solution(weight):
    answer = 0
    weight = sorted(weight, reverse = True)
    num = 1
    while True:
        if not check_num(weight, num):  # False 면 아웃
            return num
        num += 1
    return 0

def check_num(weight, num):
    for i in range(0,len(weight)):
        if weight[i] <= num :
            num -= weight[i]
    if num == 0:
        return True
    return False

# 중복이 없을때 
# def solution(weight):
#     answer = 0
#     weight = sorted(weight, reverse=True)
#     num = 1
#     int_list = [len(weight)]
#     while True:
#         if not check_num(weight,int_list, num):  # False 면 아웃
#             return num
#         num += 1
#     return 0

# def check_num(weight,int_list, num):
#     for i in range(0,len(weight)):
#         if weight[i] <= num :
#             num -= weight[i]
#             if int_list[num] > i:
#                 int_list.append(i)
#                 return True
#     return False