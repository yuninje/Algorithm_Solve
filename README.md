# Algorithm Problem Solve & Algorithm Code

## SWEA, 백준, 프로그래머스 문제 풀이 및 알고리즘 코드

### Reference
- **프로그래머스** : https://programmers.co.kr
- **SWEA ( SW Expert Academy )** https://swexpertacademy.com/main/main.do
- **백준** : https://www.acmicpc.net/


## Python Coding Tip

``` python
    import sys
    sys.setrecursionlimit(10**6)    # Maximum Recursion Dept Exceed
    
    I = sys.stdin.readline
    A = I()

    A = input()              # Memory Save 
    A = sys.stdin.readline() # Time Save

    A = [[0 for _ in range(0,N)] for __ in range(0,N)]  # X
    A = [[0] * N for _ in range(0,N)]                   # O

    arr = [list(map(int, input().split())) for _ in range(M)]

    import collections
    deq = collections.deque()



    print(" ".join(map(str, line)))                     # O

    for a in line:
        print(a, end=' ')                               # X
    print()

```