# https://programmers.co.kr/learn/courses/30/lessons/49188?language=java
# 2 <= N <= 5,000
# node : 1 ~ N
# edges <= N ( N + 1 ) // 2

def solution(N, edges):
    answer = 0
    
    
    # 1. 인접리스트 만든다.
    adj = [[] for _ in range(N+1)]
    for s, e, in edges:
        adj[s].append(e)
        adj[e].append(s)

    # 2. 사이클을 찾는다.
    
    for i in range(1,N+1):
        dfs()
    



    


    return answer

def dfs(ban, )



print('answer : 5 , my result : ' + str(solution(4,[[1,2],[1,3],[2,3],[2,4],[3,4]])))
print('answer : 0 , my result : ' + str(solution(8,[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,1],[2,7],[3,6]])))










