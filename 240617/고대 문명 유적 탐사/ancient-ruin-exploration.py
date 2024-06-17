def turn_90(sy, sx, arr):
    temp = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp[j][2 - i] = arr[sy + i][sx + j]
    for i in range(3):
        for j in range(3):
            arr[sy + i][sx + j] = temp[i][j]

def turn_180(sy, sx, arr):
    temp = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp[2 - i][2 - j] = arr[sy + i][sx + j]
    for i in range(3):
        for j in range(3):
            arr[sy + i][sx + j] = temp[i][j]

def turn_270(sy, sx, arr):
    temp = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            temp[2 - j][i] = arr[sy + i][sx + j]
    for i in range(3):
        for j in range(3):
            arr[sy + i][sx + j] = temp[i][j]

def dfs(sy, sx, value, visited, pl, cnt = 1):
    dir = [(0,-1), (-1,0), (0,1), (1,0)]
    visited[sy][sx] = True
    
    for di, dj in dir:
        dy, dx = sy+di, sx+dj
        
        if 0 <= dy < 5 and 0 <= dx < 5 and not visited[dy][dx] and field[dy][dx] == value:
            visited[dy][dx] = True
            pl.append((dy,dx))
            cnt =  dfs(dy,dx,value,visited,pl,cnt+1)
    return cnt 


def gm():
    total = 0
    place = []
    visited = [[False]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if visited[i][j]: continue
            pl = [(i,j)]
            cnt= dfs(i,j,field[i][j], visited, pl)
            if cnt >= 3:
                total += cnt                
                place.extend(pl)
    return total, place

# def fill():
#     for j in range(5):
#         for i in range(4,-1,-1):
#             if field[i][j] == 0:
#                 field[i][j] = sub.pop(0)

k, m = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(5)]
sub = list(map(int,input().split()))


for _ in range(k):
    answer = 0

    f_max = 0
    f_degree = 0
    f_yi, f_xi = 0, 0
    f_replace = []

    # 틀린 이유!! ==> 각 -> 열 -> 행 ... ㅠㅠ
    # 우선 순위가 될 수록 외부에서 진행! 가장 느리게 바뀌는 만큼 해당 값에서
    # 다른 변수들만 먼저 바뀌는 거지
    # => 자연스럽게, 회전 목표 조건 충족 ('>')
    for k in range(3):
        for j in range(3):
            for i in range(3):
                if k == 0:
                    turn_90(i, j, field)
                elif k == 1:
                    turn_180(i,j,field)
                elif k==2:
                    turn_270(i,j,field)
                # 여기서 첫번 째 유물 몇 개인지 체크
                f_total, f_place = gm()
                if f_total > f_max:
                    f_max = f_total
                    f_degree = k
                    f_yi, f_xi = i, j
                    f_replace = f_place

                if k == 0:
                    turn_270(i, j, field)
                elif k == 1:
                    turn_180(i,j,field)
                elif k==2:
                    turn_90(i,j,field)
    if f_max == 0: break
    
    answer += f_max

    # 이 부분 hash 등 방법 써서 리팩토링 가능
    if f_degree == 0:
        turn_90(f_yi, f_xi, field)
    elif f_degree == 1:
        turn_180(f_yi, f_xi, field)
    elif f_degree == 2:
        turn_270(f_yi, f_xi, field)
    
    f_replace = sorted(f_replace, key = lambda x : (x[1], -x[0]))
    for i in range(len(f_replace)):
        ri, rj = f_replace[i]
        field[ri][rj] = sub.pop(0)

    while True:       
        s_total, s_replace = gm()
        
        if s_total == 0:
            break

        answer+= s_total
        s_replace = sorted(s_replace, key = lambda x : (x[1], -x[0]))
        for i in range(len(s_replace)):
            ri, rj = s_replace[i]
            field[ri][rj] = sub.pop(0)
    print(answer, end =" ")