


#그리디 알고리즘

# 문제1 큰 수의 법칙

""" 
n,m,k=map(int,input().split())
#배열크기,더하는 횟수, 연속 조건

data=list(map(int,input().split()))
#배열 입력

result=0

data.sort()

max_1=data[-1]
max_2=data[-2]

while(True):
    for i in range(k):
        if m==0:
            break
        result+=max_1
        m-=1
    if m==0:
        break
    
    result+=max_2
    m-=1
    
print(result)
"""    

#문제2 숫자 카드 게임
""" 
n,m=map(int,input().split())

result=0

for i in range(n):
    data=list(map(int,input().split()))
    mini=200    
    
    for ii in data:
        mini=min(mini,ii)
    
    result=max(result,mini)

print(result)

 """


#문제3
#1이 될때 까지

N,K=map(int,input().split())

cnt=0

while(N!=1):
    if N%K==0:
        N//=K
        cnt+=1  
    else:
        N-=1
        cnt+=1
print(cnt)