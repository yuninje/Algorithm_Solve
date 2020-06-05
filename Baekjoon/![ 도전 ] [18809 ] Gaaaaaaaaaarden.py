# https://www.acmicpc.net/problem/18809
# 2 <= R, C <= 50
# 1 <= GREEN, RED <= 5
# 0 <= GREEN + RED <= 10
# 0 : 호수
# 1 : 배양액을 뿌릴 수 없는 땅
# 2 : 배양액을 뿌릴 수 있는 땅
# 3 : Green 배양액이 이미 퍼진 땅
# -3 : Green 배양액이 방금 퍼진 땅
# 4 : Red 배양액이 이미 퍼진 땅
# -4 : Red 배양액이 방금 퍼진 땅
# 배양액은 매 초마다 이전에 배양액이 도달한 적이 없는 인접한 땅으로 퍼짐

import sys
I = sys.stdin.readline

LAKE = 0            # 호수
CAN_NOT_WATER = 1   # 배양액을 뿌릴 수 없는 땅
CAN_WATER = 2       # 배양액을 뿌릴 수 있는 땅
GREEN = 3           # Green 배양액이 이미 퍼진 땅
RED = 4             # Red 배양액이 이미 퍼진 땅
FLOWER = 5          # 꽃
GREEN_REACHING = -3 # Green 배양액이 방금 퍼진 땅
RED_REACHING = -4   # Red 배양액이 방금 퍼진 땅

# 시뮬
def bfs(garden):
  que = []
  answer = 0
  for r in range(R):
    for c in range(C):
      if garden[r][c] == GREEN or garden[r][c] == RED:
        que.append((garden[r][c], r, c))

  while que:
    que_ = []
    changes = []

    for v, r, c in que:
      if garden[r][c] == FLOWER: # 꽃으로 변한 경우
        continue

      if v == GREEN or v == RED:
        for dr, dc in dir:
          rr = r + dr
          cc = c + dc
          
          if not (0 <= rr < R and 0 <= cc < C ):
            continue
          
          # 퍼질 수 있는 땅
          if garden[rr][cc] == 1:
            garden[rr][cc] = -v
            changes.append((rr,cc))
            que_.append((v, rr, cc))

          # 새로 배양액이 퍼진 땅이면서 지금 퍼지는 배양액과 색이 다른 경우 >> 꽃
          elif garden[rr][cc] < 0 and garden[rr][cc] != -v:
            garden[rr][cc] = FLOWER
            answer += 1
    
    # 1초 지남
    que = que_
    for r, c in changes:
      if garden[r][c] != FLOWER:
        garden[r][c] = abs(garden[r][c])

  answer_list[0] = max(answer_list[0], answer)
  return

# 배양액 뿌린 땅 설정
def dfs(i, unused, green, red):
  if i == len(possible_areas):
    for r in range(R):
      for c in range(C):
        garden_[r][c] = garden[r][c]
    bfs(garden_)
    return
  r, c = possible_areas[i]

  # 배양액 사용 x
  if unused + 1 <= UNUSED_AREA_COUNT:
    garden[r][c] = CAN_NOT_WATER # 배양액을 뿌릴 수 없는 땅
    dfs(i+1, unused+1, green, red)
    garden[r][c] = CAN_WATER # 배양액을 뿌릴 수 있는 땅으로 복구

  # 초록색 배양액
  if green + 1 <= GREEN_COUNT:
    garden[r][c] = GREEN # Green 배양액이 방금 퍼진 땅
    dfs(i+1, unused, green+1, red)
    garden[r][c] = CAN_WATER # 배양액을 뿌릴 수 있는 땅으로 복구

  # 빨강색 배양액
  if red + 1 <= RED_COUNT:
    garden[r][c] = RED # Red 배양액이 방금 퍼진 땅
    dfs(i+1, unused, green, red+1)
    garden[r][c] = CAN_WATER # 배양액을 뿌릴 수 있는 땅으로 복구


dir = [(1,0), (-1,0), (0,1), (0,-1)]
R, C, GREEN_COUNT, RED_COUNT = map(int, I().split())
garden = [list(map(int, I().split())) for _ in range(R)]
garden_ = [[0] * C for _ in range(R)]
possible_areas = []

for r in range(R):
  for c in range(C):
    if garden[r][c] == CAN_WATER: # 뿌릴 수 있는 땅
      possible_areas.append((r,c))

UNUSED_AREA_COUNT = len(possible_areas) - RED_COUNT - GREEN_COUNT

answer_list = [0]
dfs(0, 0, 0, 0)
print(answer_list[0])
