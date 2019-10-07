# https://www.acmicpc.net/problem/1074
def dfs(sr,er,sc,ec):

    if er - sr == 1:
        if r == sr:
            if c == sc:
                return 0
            else:
                return 1
        else:
            if c == sc:
                return 2
            else:
                return 3

    mr = (sr + er) // 2
    mc = (sc + ec) // 2
    answer = 0
    group = [[sr,mr,sc,mc], [sr,mr,mc+1,ec], [mr+1,er,sc,mc],[mr+1,er,mc+1,ec]]
    for ssr, eer, ssc, eec in group:
        if ssr <= r and r <= eer and ssc <= c and c <= eec:
            answer += dfs(ssr,eer,ssc,eec)
            return answer
        answer += (eer - ssr + 1) ** 2

N,r,c = list(map(int,input().split()))
print(dfs(0,2 ** N-1,0,2 ** N-1))
