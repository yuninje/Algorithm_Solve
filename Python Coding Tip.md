## Python Coding Tip

``` python
    import sys
    sys.setrecursionlimit(10**6)    # Maximum Recursion Dept Exceed

    A = input()              # Memory Save 
    A = sys.stdin.readline() # Time Save

    A = [[0 for _ in range(0,N)] for __ in range(0,N)]  # X
    A = [[0] * N for _ in range(0,N)]                   # O
```