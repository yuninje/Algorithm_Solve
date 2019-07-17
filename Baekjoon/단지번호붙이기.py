def solution():
    N = int(input())

    str_list = []
    for _ in range(0,N):
        str_list.append(input())

    origin_list = []
    for i in range(0,N):
        list_ = []
        for j in range(0,N):
            list_.append(int(str_list[i][j]))
        origin_list.append(list_)    

    #============================================
    bool_list = [[False for _ in range(0,N+2)] for __ in range(0,N+2)]
    for i in range(0,N+2):
        bool_list[0][i] = True
    for i in range(0,N+2):
        bool_list[N+1][i] = True
    for i in range(0, N+2):
        bool_list[i][0] = True
    for i in range(0,N+2):
        bool_list[i][N+1] = True

    count = []
    count_index = 0
    for i in range(1, N+1):
        for j in range(1,N+1):
            if not bool_list[i][j] and origin_list[i-1][j-1]==1:
                count.append(0)
                dfs(origin_list, bool_list, i,j,count, count_index)
                count_index += 1
    
    print(len(count))
    count  = sorted(count)
    for c in count:
        print(c)
    
def dfs(origin_list, bool_list, i, j, count, count_index):
    if not bool_list[i][j] and origin_list[i-1][j-1] == 1:
        bool_list[i][j] = True

        count[count_index] += 1
        dfs(origin_list, bool_list, i, j+1, count, count_index) # 동
        dfs(origin_list, bool_list, i, j-1, count, count_index) # 서
        dfs(origin_list, bool_list, i+1, j, count, count_index) # 남
        dfs(origin_list, bool_list, i-1, j, count, count_index) # 북
    
solution()