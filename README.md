# Algorithm Problem Solve & Algorithm Code

## SWEA, 백준, 프로그래머스 문제 풀이 및 알고리즘 코드




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

### Big-O [Link](https://cjh5414.github.io/big-o-notation/)
- 시간복잡도 : big-O 에 대한 시간 개념. 알고리즘의 수행 시간
- 공간복잡도 : big-O 에 대한 공간 개념. 알고리즘의 필요 메모리

### DFS, BFS
- DFS
- BFS

### 탐색
- Linear Search
- Binary Search

### 정렬 [Link](https://www.toptal.com/developers/sorting-algorithms)
- Bubble Sort
  ```python
  def bubble_sort(arr):
      N = len(arr)
      
      flag = True
      for i in range(N-1, -1, -1):
          if flag:
              flag = False  
          for j in range(i):
              if arr[j] > arr[j+1]:
                  swap(arr, j+1, j)
                  flag = True
              else:
                  break
  ```
- Selection Sort
  ```python
  def selection_sort(arr):
      N = len(arr)
      
      for i in range(N):
          midx = i
          for j in range(i+1, N):
              if arr[midx] > arr[j]:
                  midx = j
          swap(arr, i, midx)
  ```
- Insertion Sort
  ```python
  def insertion_sort(arr):
      N = len(arr)
      
      for i_ in range(1,N):
          i = i_
          for j in range(i_-1, -1, -1):
              if arr[j] > arr[i]:
                  swap(arr, i, j)
                  i = j
              else:
                  break
  ```
- Merge Sort
  ```python
  def merge_sort(arr, si, ei):
      if si == ei-1:
          return [arr[si]]
      mi = (si + ei) // 2

      # Devide
      left = merge_sort(arr, si, mi)
      right = merge_sort(arr, mi, ei)

      li = 0
      li_max = mi - si
      ri = 0
      ri_max = ei - mi
      result = []
      
      
      # Conquer
      while li != li_max and ri != ri_max:
          if left[li] < right[ri]:
              result.append(left[li])
              li += 1
          else:
              result.append(right[ri])
              ri += 1
      for i in range(li,li_max):
          result.append(left[i])
      for i in range(ri,ri_max):
          result.append(right[i])

      return result
  ```
- Heap Sort
  ```python

  ```
- Quick Sort
  ```python

  ```
- Counting Sort
  ```python

  ```
- Radix Sort
  ```python

  ```
- Shell Sort [Link](https://gmlwjd9405.github.io/2018/05/08/algorithm-shell-sort.html)
- Tim Sort [Link](http://blog.naver.com/PostView.nhn?blogId=talag&logNo=221020181491)


### 최단 경로
- 다익스트라[Link](https://ratsgo.github.io/data%20structure&algorithm/2017/11/26/dijkstra/)
    ```python

    ```
- 플로이드 워셜[Link](https://engkimbs.tistory.com/371)
    ```python

    ```
- 벨만 포드 [Link](https://ratsgo.github.io/data%20structure&algorithm/2017/11/27/bellmanford/)
    ```python

    ```

### MST
- 프림
    ```python

    ```
- 크루스칼
    ```python

    ```



### Prime Number
- 에라토스테네스의 체 ( Eratosthenes' sieve )
    ```python
    def find_prime_num(N):
        arr = [True] * N
        for n in range(2,N):
            if arr[n]:
                print(n, end=' ')
                for nn in range(2 * n, N, n): # 2n, 3n, 4n ...
                    arr[nn] = False
    ```

### GCD, LCM
- 유클리드 호제법
  - GCD
    ```python
    def find_GCD(a,b): # 1 <= a , b 
        while b != 0:
            n = a % b
            a = b
            b = n
        return a
    ```
  - LCM
    ```python
    def find_LCM(a,b):
        return a * b // find_GCD(a, b)
    ```


### Dynamic Programming
- 이항계수
    ```python
    def combination(n,r):   # N >= n >= r >= 0
        if dp[n][r] == -1:  # default 값
            if r == 0 or r == n:
                dp[n][r] = 1
            else:
                dp[n][r] = combination(n-1,r-1) + combination(n-1,r)
            
        return dp[n][r]
    ```


- 피보나치 수열

### 집합론
- Combination
    ```python
    def combination(before, count, m):
        if count == m:
            # arr 에 관한 작업
            return

        for n in range(before + 1, N):
            if visit[n]:
                continue
            result[count] = n
            combination(n, count + 1, m)

    result = [0] * N
    combination(-1, 0, m)
    ```
- permutation
    ```python
    def permutation(count):
        if count == N:
            # arr 에 관한 작업
            return

        for n in range(N):
            if visit[n]:
                continue
            result[count] = n
            permutation(count+1)

    result = [0] * N
    permutation(0)
    ```
- Subset
    ```python
    def sunset(now, N):
        if now == N:
            # arr 에 관한 작업
            return
        sunset(now+1)
        arr.append(now)
        sunset(now+1)

    arr = []
    sunset(0, N) # 0부터 N-1 까지의 숫자 집합의 부분집합
    ```

### NP
- TSP
    ```python
    def tsp(start, curr, visit):    # 시작, 이전, 방문정보
        if visited == (1<<N) - 1:
            return adj[curr][start]

        if( dp[curr][visit] == INF): # dafult 값
            for n in range(N):
                if (visit & 1 << i) or adj[curr][n] == -1:
                    continue
                dp[curr][visit] = min(dp[curr][visit], tsp(start, n, visit) + adj[curr][n]))

        return dp[curr][visit]

    INF = 999999999
    dp = [[INF] * N for _ in range(1<<N)]
    for n in range(N):
        tsp( n, n, 1 << n )
    ```


### Reference
- **프로그래머스** : https://programmers.co.kr
- **SWEA ( SW Expert Academy )** https://swexpertacademy.com/main/main.do
- **백준** : https://www.acmicpc.net/