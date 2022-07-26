#미로찾기
from collections import deque
n,m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input())))
    #상하좌우
dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=n or ny >=m or nx<0 or ny<0:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx,ny))

    return maps
print(bfs(0,0))