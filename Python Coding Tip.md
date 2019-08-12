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

    
    import collections
    deq = collections.deque()



    print(" ".join(map(str, line)))                     # O

    for a in line:
        print(a, end=' ')                               # X
    print()

```