# https://www.acmicpc.net/problem/1992
import sys
sys.setrecursionlimit(10**6)
I = sys.stdin.readline


def dfs(sr,er,sc,ec):
    mr = (sr+er) // 2
    mc = (sc+ec) // 2

    if er - sr == 0:
        return Map[sr][sc]
    
    str1 = dfs(sr,mr,sc,mc)
    str2 = dfs(sr,mr,mc+1,ec)
    str3 = dfs(mr+1,er,sc,mc)
    str4 = dfs(mr+1,er,mc+1,ec)

    if str1 == str2 == str3 == str4:
        if str1 == '1':
            return '1'
        elif str1 == '0':
            return '0'
        return '('+str1+str2+str3+str4+')'
    else:
        return '('+str1+str2+str3+str4+')'


N = int(I())
Map = [list(I().strip()) for _ in range(N)]
print(dfs(0,N-1,0,N-1))