

#1주차-----------------------------------------------------------------

""" class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        else :
            reverse=0
            temp=x
            while(temp>0):
                reverse=reverse*10+temp%10
                temp//=10
            return x==reverse
test_case=Solution()
print(test_case.isPalindrome(121))
print(test_case.isPalindrome(-121))
print(test_case.isPalindrome(10))  """     


#-------------------------------------------
#https://leetcode.com/problems/valid-parentheses/description/

""" class Solution:
    def isValid(self, s: str) -> bool:
        
        pair={')':'(','}':'{',']':'['}
        stack=[]
        for i in s:
            if i in pair.values():
                stack.append(i)
                #열린 괄호는 스택에 추가
            else:
                if not stack or stack[-1]!=pair[i]:
                    return False
                stack.pop()
        return not stack
                
sol=Solution()
print(sol.isValid('((((((({{{{{{[[[[[[]]]]]]}}}}}})))))))'))

 """


#https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

""" from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_last_index=m-1
        nums2_last_index=n-1 
        in_position=m+n-1
        
        while(nums2_last_index>=0): #nums2 인덱스 기준으로 반복문 실행
            if nums1_last_index>=0 and nums1[nums1_last_index] > nums2[nums2_last_index]: 
                #만약 nums1의 요소가 nums2보다 크다면
                
                #0보다 큰 조건을 빼서 런타임 에러 떳음 <= 참고 바람.
                
                nums1[in_position]=nums1[nums1_last_index]
                nums1_last_index-=1
                
            else: #만약 nums2 요소가 nums1보다 크다면 
                nums1[in_position]=nums2[nums2_last_index] 
                #삽입 위치에 nums2 요소를 하나 넣어줍니다.
                nums2_last_index-=1
            
            in_position-=1 #삽입후에 포지션 조정
             
sol=Solution()
sol.merge([1,2,3,0,0,0],3,[2,5,6],3)
 """




#2주차-----------------------------------------------------------------
#--------------------------------------------------
#https://leetcode.com/problems/remove-element/submissions/1600262320/?envType=study-plan-v2&envId=top-interview-150



""" class Solution(object):
    def removeElement(self, nums, val):
        cnt=0
        for i in range(len(nums)): #nums 배열 순회 작업 시작
            if nums[i] != val: #이때 만약 nums요소가 val과 같은 경우
                nums[cnt]=nums[i]
                cnt+=1
        return cnt
sol=Solution()

print(sol.removeElement([0,1,2,2,3,0,4,2],2))
 """

 
#----------------------------------------------------------------------------------
#https://school.programmers.co.kr/learn/courses/30/lessons/12981?language=python3


""" def solution(n, words):
    answer = [0,0]
    err_token=0
    temp=words[0][0]
    
    used_word=set() #중복 검사를 위한 set 생성
    used_word.add(words[0])
    
    for i in range(len(words)):
        if len(words[i])==1: #만약 한 글자를 말한다면 바로 종료
            err_token=1
            break
        if temp!=words[i][0] and i!=0:#만약 끝말잇기가 안된다면 종료
            err_token=1
            break
        
        if words[i] in used_word and i!=0:
            err_token=1
            break
        
        #---------------------------------
        
        #-----------------------------
        
        temp=words[i][-1] #마지막 단어 저장
        used_word.add(words[i])
        #--------------------------------------------
    if err_token :
        answer=[]
        answer.append(i%n+1) # 누가 틀렸는지
        answer.append((i//n)+1) # 몇 번쨰 턴인지
        return answer
    else:
        return answer
    

print(solution(5,	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
  """
 
 
#3주차-----------------------------------------------------------------

#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150


""" 
class Solution(object):
    def removeDuplicates(self, nums):
        list_position=1
        for i in range(1,len(nums)):    
            if nums[list_position-1]!=nums[i]:
                nums[list_position]=nums[i]
                list_position+=1

        return list_position
    
    
sol=Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
 """





#https://school.programmers.co.kr/learn/courses/30/lessons/12980

""" 
def solution(n):
    ans = 0

    while(n!=0):
        if n%2==0:
            n//=2
        else:
            ans+=1
            n-=1        
    return ans
 """






# 4주차 -------------------------------------------------------------------------

#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150



""" class Solution(object):
    def removeDuplicates(self, nums):
        list_position=1
        for i in range(1,len(nums)):    
            if list_position < 2 or nums[list_position-2]!=nums[i]:
                nums[list_position]=nums[i]
                list_position+=1

        return list_position
    
    
sol=Solution()
print(sol.removeDuplicates([0,0,1,1,1,1,2,3,3]))
 """
 
 
 
 
#5주차-----------------------------------------------------------------
#https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150



""" class Solution(object):
    def rotate(self, nums, k):
        N=len(nums)
        k=k%N
        nums[:]=nums[-k:]+nums[:-k]
        return nums

sol=Solution()
print(sol.rotate([1,2,3,4,5,6,7],3))

"""


#https://school.programmers.co.kr/learn/courses/30/lessons/12985?language=python3

""" 
def solution(n,a,b):
    answer = 0
    
    while(a!=b):
        a=(a+1)//2
        b=(b+1)//2
        answer+=1
    return answer
print(solution(8,1,2))
 """

 
#6주차-----------------------------------------------------------------

#https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150


""" 
class Solution(object):
    def isPalindrome(self, s):
        
        new_s=[]
        for i in s:
            if i.isalnum():
                new_s.append(i.lower())
        return new_s[:]==new_s[::-1]
        
sol=Solution()
print(sol.isPalindrome("race a ecar"))
 """


#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

""" 
class Solution(object):
    def maxProfit(self, prices):
        
        N=len(prices)
        min_price=prices[0]
        my_profit=0
    
        for i in range(N):
            if prices[i]<min_price: #최소값 갱신
                min_price=prices[i]
            if prices[i]-min_price>my_profit: #이익 갱신
                my_profit=prices[i]-min_price
                
        return my_profit
    
sol=Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
 """

#7주차---------------------------------------------

#https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150

""" 
class Solution(object):
    def majorityElement(self, nums):
        
        #보이어 무어 알고리즘
        
        result=None
        cnt=0
        
        for num in nums:
            if cnt==0:
                result=num
            if result==num:
                cnt+=1
            else:
                cnt-=1
            
        return result
    
    
sol=Solution()
print(sol.majorityElement([2,2,1,1,1,2,2]))
 """


#https://school.programmers.co.kr/learn/courses/30/lessons/131701

""" 
def solution(elements):
    answer = 0
    elements*=2 #배열의 길이를 넘어가면 계산이 조금 복잡해짐
    N=len(elements) #배열 길이 (원본 2배)
    sum_get=set() #중복제거 sum_get
    
    part_sum=[0]*(N+1)

    for i in range(1,N+1):
        part_sum[i]=part_sum[i-1]+elements[i-1]
    
    for length in range(1,(N)//2+1):
        for start_pos in range(0,(N)//2):
            mini_sum=part_sum[start_pos+length]-part_sum[start_pos]
            sum_get.add(mini_sum)
            
    answer=len(sum_get)
    return answer
    
    
print(solution([7,9,1,1,4]))

 """

"""1234"""






