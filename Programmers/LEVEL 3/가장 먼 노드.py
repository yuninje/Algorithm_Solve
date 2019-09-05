def solution(n, edge):
    adj = [[] for _ in range(n+1)]
    for a,b in edge:
        adj[a].append(b)
        adj[b].append(a)
    
       
    
    return bfs(adj,n) 

def bfs(adj,n):
    count = n
    visit = [False] * (n+1)
    visit[1] = True
    queue = [1]
    while queue:
        queue_ = []
        before = count
        for q in queue:
            count -= 1
            for q_ in adj[q]:
                if visit[q_]:
                    continue
                visit[q_] = True
                queue_.append(q_)
        if count == 0:
            return before
        queue = queue_