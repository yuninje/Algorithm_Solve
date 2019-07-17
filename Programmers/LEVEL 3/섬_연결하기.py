from operator import itemgetter
def solution(n, costs):
    answer = 0
          
    costs = sorted(costs, key= lambda x: (x[2],x[0],x[1]) )
    
    team = [-1 for _ in range(0,n)]
    team_list = []
    new_team_count = 0
    for i in range(0, len(costs)):
        if team[costs[i][0]] == -1: #(X, ?)  
            if team[costs[i][1]] == -1:      #(X, X)
                team_list.append([costs[i][0], costs[i][1]])
                answer += costs[i][2]
                team[costs[i][0]] = new_team_count
                team[costs[i][1]] = new_team_count
                new_team_count += 1
            else:                           #(X, O)
                for t in range(0,len(team_list)):
                    if costs[i][1] in team_list[t]:
                        answer += costs[i][2]
                        team_list[t].append(costs[i][0])
                        team[costs[i][0]] = t
                        break
        else: #(O, ?)
            if team[costs[i][1]] == -1:      #(O, X)
                answer += costs[i][2]
                team_list[team[costs[i][0]]].append(costs[i][1])
                team[costs[i][1]] = team[costs[i][0]]
            else:                           #(O, O)
                if team[costs[i][0]] == team[costs[i][1]]:  # SAME
                    sameTeam = True         # 아무것도 안함
                else:                                       # DIFF
                    answer += costs[i][2]   # answer 증가
                    remove_team = team[costs[i][1]]
                    for move in team_list[remove_team]:
                        team_list[  team[costs[i][0]]  ].append(move)
                    for m in team_list[remove_team]:
                        team[m] = team[costs[i][0]]
                    team_list[remove_team] = []
    return answer