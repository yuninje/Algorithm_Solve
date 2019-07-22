# 각 카드에는 양의 정수 하나가 적혀있다. 같은 숫자 여러장 가능.
# 짝수개의 카드를 무작위로 섞은 뒤 개수의 두 더미로 나누어 하나는 왼쪽, 하나는 오른쪽

# 언제든지. 왼쪽 카드만 버릴수있다.
# 왼쪽카드와 오른쪽카드 둘 모두 버릴 수 있다. > 얻는 점수 X
# left > right   이면 오른쪽 카드를 버릴 수 있다.  >> 오른쪽 카드에 적힌 점수를 얻는다.

# 양쪽에 카드가 없으면 게임 끝.  얻은 점수의 합이 최종점수

# 3 2 5     2 4 1   
#  

def dfs(left, right, li, ri, answer):
    global answer_list
    #print("li : " + str(li) + "   ri : " + str(ri) + "  answer : " + str(answer) + " =======" )
    while True:
        if li >= len(left) and ri <len(right):
            return
        if ri >= len(right):
            break
            
        if left[li] > right[ri]:
            answer += right[ri]
            ri += 1
        else :
            #print("========================else")
            # 동반
            dfs(left, right, li+1, ri+1, answer)
            # 혼자
            dfs(left, right, li+1, ri, answer)
            break
        
    answer_list.append(answer)



def solution(left, right):
    answer = 0
    
    dfs(left, right, 0, 0, 0)
    
    return max(answer_list)

answer_list = []