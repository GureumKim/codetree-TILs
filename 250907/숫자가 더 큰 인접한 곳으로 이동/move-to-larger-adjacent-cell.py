n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

# Please write your code here.
# 우선 순위는 상, 하, 좌, 우
# 여기서 상 - 우 가는 중에 큰거 나오면 바로 이동
# 상,하, 좌, 우 -> 다 못 가면 그 때 
dx = [0, 0, -1, 1]
dy = [-1, 1 , 0, 0]

ans = [a[r][c]]

while True:
    for i in range(4):
        dr = r + dy[i]
        dc = c + dx[i]
        if 1<= dr <= n and 1 <= dc <= n:
            if a[dr][dc] > a[r][c]:
                ans.append(a[dr][dc])
                r = dr
                c = dc
                break
    else:
        print(*ans)
        break