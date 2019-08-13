# https://www.acmicpc.net/problem/2096
# 1 <= N <= 100000
# 숫자 : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# print(MAX, MIN)


N = int(input())
arr = []
for n in range(0,N):
    arr.append(list(map(int, input().split())))

max_list = [[arr[0][0], arr[0][1], arr[0][2]] for _ in range(0,2)] 
min_list = [[arr[0][0], arr[0][1], arr[0][2]] for _ in range(0,2)] 
# 홀수 : 위에서 아래로 ( 0 -> 1 )
# 짝수 : 아래에서 위로 ( 1 -> 0 )
for n in range(1,N):
    r = n%2             # 1  0  
    
    rr = (r +1 ) %2     # 0  1
    max_list[r][0] = max(max_list[rr][0], max_list[rr][1]) + arr[n][0]
    max_list[r][1] = max(max_list[rr][0], max_list[rr][1], max_list[rr][2]) + arr[n][1]
    max_list[r][2] = max(max_list[rr][1], max_list[rr][2]) + arr[n][2]
    min_list[r][0] = min(min_list[rr][0], min_list[rr][1]) + arr[n][0]
    min_list[r][1] = min(min_list[rr][0], min_list[rr][1], min_list[rr][2]) + arr[n][1]
    min_list[r][2] = min(min_list[rr][1], min_list[rr][2]) + arr[n][2]

# (N-1) % 2
print(max(max_list[(N-1) %2]),end=' ')
print(min(min_list[(N-1) %2]),end=' ')