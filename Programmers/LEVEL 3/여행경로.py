answer_list = []
def solution(tickets):
    arr = [False for _ in range(len(tickets))]
    tickets = sorted(tickets, key = lambda x: (x[0], x[1]))
    dfs(tickets, arr, ["ICN"], 1)
    return answer_list

def dfs(tickets, arr, answer,count):
    global answer_list
    if len(answer_list) != 0:
        return
    if count == len(tickets)+1:
        answer_list = answer.copy()
    else:
        for i in range(0,len(tickets)):
            if not arr[i] and answer[count-1] == tickets[i][0]:
                arr[i] = True
                count += 1
                answer.append(tickets[i][1])
                dfs(tickets, arr.copy(), answer.copy(), count)
                arr[i] = False
                count -= 1
                del answer[-1]