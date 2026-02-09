

#4-1 상하좌우

""" 
N=int(input())
pos_list=input().split()

x,y=1,1

for i in pos_list:
    
    if i == 'U':
        if y<=1:
            pass
        else:
            y-=1
    elif i== "R":
        if x>=N:
            pass
        else:
            x+=1
    elif i== "D" :
        if y>=N:
            pass
        else:
            y+=1
    else:
        if x<=1:
            pass
        else:
            x-=1
            
print(x,y)

 """

#4-2 시각

N = int(input())

minute,sec=60,60

count=0
result=0

for i in range(N+1):
    for ii in range(minute):
        for iii in range(sec):
            if str(N) in str(i) + str(ii)+str(iii):
                result+=1     
            
print(result)
    
    
    