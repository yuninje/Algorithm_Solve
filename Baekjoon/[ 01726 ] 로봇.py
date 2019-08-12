def bfs():
    q.append([start[0],start[1],start[2], False])
    order = 0
    while q:
        count = len(q)
        print("===============================================count : " + str(count) + "  order : " + str(order))
        while count != 0:
            count -= 1
            now = dequeue()
            
            if dp[now[0]][now[1]] == -1:
                dp[now[0]][now[1]] = order
            elif dp[now[0]][now[1]] +1 < order:
                print("now : " + str(now) + "  이미 방문함")
                continue


            
            if area[now[0]][now[1]] == 1:               # 벽
                print("now : " + str(now) + "  벽임")
                continue

            if now[0] == end[0] and now[1] == end[1]:   # 도착
                print("now : " + str(now) + "  도착함")
                if now[2] == end[2]:
                    return order
                elif (now[2] -1 ) // 2 == (end[2] -1) //2:
                    return order +2
                else:
                    return order+1

            print("now : " + str(now) )

            

            if area[now[0] + dir[now[2]][0] * 1 ][ now[1] + dir[now[2]][1] * 1] == 0:
                enqueue([now[0] + dir[now[2]][0] * 1 , now[1] + dir[now[2]][1] * 1, now[2], False]) 
                if area[now[0] + dir[now[2]][0] * 2 ][ now[1] + dir[now[2]][1] * 2] == 0: 
                    enqueue([now[0] + dir[now[2]][0] * 2 , now[1] + dir[now[2]][1] * 2, now[2], False])
                    if area[now[0] + dir[now[2]][0] * 3 ][ now[1] + dir[now[2]][1] * 3] == 0: 
                        enqueue([now[0] + dir[now[2]][0] * 3 , now[1] + dir[now[2]][1] * 3, now[2], False]) 



            if now[2] == 1 or now[2] == 2 and not now[3]:   # 동서                                          
                enqueue([now[0],now[1], 3, True])           # 남            
                enqueue([now[0],now[1], 4, True])           # 북
            elif now[2] == 3 or now[2] == 4 and not now[3]: # 남북                        
                enqueue([now[0],now[1], 1, True])           # 동             
                enqueue([now[0],now[1], 2, True])           # 서
            
        order += 1

def dequeue():
    popObject = q[0]
    del q[0]
    return popObject

def enqueue(object):
    q.append(object)

dir = [[],[0,1], [0,-1],[1,0], [-1,0]] 
R,C = list(map(int,input().split()))
area = [[1] * (C+6) for _ in range(0,R+6)]
for r in range(3,R+3):
    line = input().split()
    for c in range(3, C+3):
        area[r][c] = int(line[c-3])

start = list(map(lambda x : int(x)+2, input().split()))
start[2] -= 2
end = list(map(lambda y : int(y)+2, input().split()))
end[2] -= 2

dp =[[-1] * (C+6) for _ in range(0,R+6)]
q = []
print(bfs())

for d in dp:
    print(d)