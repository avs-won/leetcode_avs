"""1"""

import sys

P,N=map(int,sys.stdin.readline().rstrip().split())
#피로도 200미만인 경우 장신구 제작
# N=만들 수 있는 장신구 개수


result=0
pirodo = list(map(int, input().split()))
pirodo.sort()
#최대값을 얻기 위해서 정렬 필요


for i in pirodo:
    if P>=200:
        break
    P+=int(i)
    result+=1

print(result)

#195 4
#20 1 8 1

'''
import sys

def dfs(c):
    answer_dfs.append(c) #방문 노드 추가
    visited[c]=1 #방문 완료
    
    for n in adj[c]:
        if not visited[n]:
            dfs(n)
            
def bfs(s):
    q=[]
    
    q.append(s)
    
    answer_bfs.append(s)
    visited[s]=1
    
    while(q):
        c=q.pop()
        for n in range(adj[c]):
            if not visited(n):
                q.append(n)
                visited[n]=1
                
N,M,V=map(int,sys.stdin.readline().rstrip().split())

adj=[[] for _ in range(N+1)]

for _ in range(M):
    start,end=map(int,input().split())
    adj[start].append(end)
    adj[end].append(start)
#----------------------------------    
#정점 번호가 작은 것 부터 가니 오름차순 정렬이 필요

for i in range(N+1):
    adj[i].sort()
    
#-----------------------------------------------

visited=[0]*(N+1)
answer_dfs=[]
dfs(V)


visited[0]*(N+1)
answer_bfs=[]
bfs(V)

#--출력------------------------------------
print(*answer_dfs)
print(*answer_bfs)
'''