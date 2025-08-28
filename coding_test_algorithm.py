


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
""" 
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
"""


#모험가 길드

""" 
N=int(input())
people = list(map(int,input().split()))

people.sort()
result=0

temp=[]

for i in range(N):
    temp.append(people[i])
    if len(temp) == people[i]:
        result+=1
        temp=[]
    else:
        pass

print(result)
""" 




#곱하기 혹은 더하기
""" 
S=input()
result=int(S[0])

for i in range(1,len(S)):
    num=int(S[i])
    if result<=1 or num<=1:
        result+=num
    else:
        result*=num 
    

print(result)
 """



#문자열 뒤집기
""" 
S=input()

cnt_0=0
cnt_1=0

if S[0]='0':
    cnt_0+=1
else:
    cnt_1+=1

for i in range(len(S)-1):
    if S[i]!=S[i+1]:
        if S[i]=='0':
            cnt_0+=1
        else:
            cnt_1+=1

print(min(cnt_0,cnt_1))
"""
 
 

#문제 4 만들 수 없는 금액
""" 
N = int(input())
data = list(map(int,input().split()))
data.sort()

res=1

for i in data:
    if res < i :
        break
    else:
        res+=i
print(res)
"""


#문제 5 볼링공 만들기
""" 
N,M = map(int,input().split())
balls=list(map(int,input().split()))

array=[0]*11

for i in balls:
    array[i]+=1
    
result=0

for i in range(1,M+1):
    N-=array[i]
    result += array[i]*N
    
print(result)
 """

#무지의 먹방 라이브

from operator import itemgetter

def solution(food_times, k):
    foods=[] #음식 저장 리스트
    n = len(food_times)  #음식 개수
    
    for i in range(n):
        foods.append((food_times[i],i+1)) #음식 시간, 번호 튜플로 삽입
    
    foods.sort() #음식 시간 작은 순서대로 정렬한다.
    
    pre_time = 0
    for i , food in enumerate(foods):
        delta = food[0] - pre_time
        
        if delta != 0 :
            minus_time=delta*n
            if minus_time <= k :
                k-=minus_time
                pre_time = food[0]
            else :
                k %= n
                temp = sorted(foods[i:],key = itemgetter(1)) #남은 음식을 다시 적은 시간순이 아닌 번호 순서대로
                
                return temp[k][1]
        n-=1
    
    return -1


