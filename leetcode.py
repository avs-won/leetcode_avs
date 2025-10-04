

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


""" def solution(elements):
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


#8주차 -------------------------------------------------------------------
#https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150

"""  
class Solution(object):
    def canJump(self, nums):
        
        n=len(nums)
        
        max_dis=0
        
        for i in range(n):
            
            if i>max_dis:
                return False
            else:
                max_dis=max(max_dis,i+nums[i])

        return True
 """

#https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

""" 
from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        rans_cnt=Counter(ransomNote)
        mag_cnt=Counter(magazine)
        
        for c in ransomNote:
            if mag_cnt[c]==0:
                return False
            mag_cnt[c]-=1
            
        return True
 """


#9주차 -----------------------------------------------
#https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150

""" 
class Solution(object):
    def lengthOfLastWord(self, s):
        
        result=0
        flag=False
        s=reversed(s)
        
        for i in s:
            if i != ' ':
                flag=True
                result+=1
                
            elif i == ' ' and flag == True:
                break
            
        return result
"""   


#https://leetcode.com/problems/roman-to-integer/?envType=study-plan-v2&envId=top-interview-150
""" 
class Solution(object):
    def romanToInt(self, s):
        roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
                    }
        
        result=0
        
        
        for i in range(len(s)-1):
            current=roman_map[s[i]]
            next_symbol=roman_map[s[i+1]]
            
            if current < next_symbol:
                result-=current
            else:
                result+=current
            
        result+=roman_map[s[-1]]
        
        return result
 """


#10주차----------------------------------------------------------------------------------
#https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150

""" 
class Solution(object):
    def summaryRanges(self, nums):
        result=[] #결과 배열
        start_pos=0 #시작 지점 위치 정보
        if not nums:
            return []
        
        for i in range(len(nums)-1):
            
            if nums[i]+1 == nums[i+1]: #만약 연속된 숫자라면
                pass
            else : #연속되지 않는다면
                
                if nums[start_pos]==nums[i]:
                    result.append(str(nums[i]))
                else:
                    result.append(f"{nums[start_pos]}->{nums[i]}")
                
                start_pos=i+1 #새로운 시작 점
                
        
        if start_pos == len(nums) - 1:  #마지막 원소가 1개라면 
            result.append(str(nums[start_pos]))
        else: # 그렇지 않다면
            result.append(f"{nums[start_pos]}->{nums[-1]}")
    
        return result
    
sol=Solution()

print(sol.summaryRanges([0,1,2,5,6,7]))
 """


#https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

""" 
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split() #좌우 공백 제거 
        result=' '.join(s[::-1])


        return result


sol=Solution()

print(sol.reverseWords("  hello world  "))
 """

#11주차 ------------------------------------------------

#https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

""" 
class Solution(object):
    def isSubsequence(self, s, t):

        i,j=0,0
        
        while i< len(s) and j<len(t):
            if s[i] == t[j] :
                i+=1
            j+=1

        if i == len(s):
            return True
        else:
            return False
    
sol = Solution()

print(sol.isSubsequence("abc","akfbdkce"))
            
 """            


#https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150

""" 
class Solution(object):
    def simplifyPath(self, path):
        
        directory=path.split('/')
        stack=[]
                
        for i in directory:
            if i == '' or i == '.' : 
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else :
                stack.append(i)
    
        return '/'+'/'.join(stack)
                
sol=Solution()
print(sol.simplifyPath("/.../a/../b/c/../d/./"))
 """


#https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150
""" 
class Solution(object):
    def longestCommonPrefix(self, strs):
        
        temp=strs[0]
        
        for i in strs[1:]:
            while not i.startswith(temp):
                temp=temp[:-1]
            if not temp:
                return ""
        return temp
    
    
sol=Solution()

print(sol.longestCommonPrefix(["flower","flow","flight"]))
 """
 
 
#12주차 ------------------------------------------------

#https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-interview-150


# Definition for singly-linked list.
""" 
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution(object):
    def hasCycle(self, head):
        fast=head
        while fast and fast.next:
            head=head.next
            fast=fast.next.next
            if head is fast:
                return True
        return False
    
node1=ListNode(3)
node2=ListNode(2)
node3=ListNode(0)
node4=ListNode(-4)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node2

sol=Solution()
print(sol.hasCycle(node1))
        
      """   
        
        
        
#개인
#https://leetcode.com/problems/jump-game-ii/submissions/?envType=study-plan-v2&envId=top-interview-150

""" 
class Solution(object):
    def jump(self, nums):
        result=0
        left,right=0,0
        
        while right < len(nums)-1:
            farthest = 0
            for i in range(left,right+1):
                farthest=max(farthest,i+nums[i])
            left=right+1
            right=farthest
            result+=1
        return result
    
sol=Solution()
print(sol.jump([2,3,1,1,4]))
 """
        
#https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
""" 
from collections import deque

class Solution(object):
    # def maxDepth(self, root):
    #     if not root:
    #         return 0
    #     return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
    
    def maxDepth(self,root):
        if not root:
            return 0
        level=0
        q=deque([root])
        while q:
            
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            level+=1
        return level
 """    
    


#13주차 ------------------------------------------------
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii?envType=study-plan-v2&envId=top-interview-150

""" 
class Solution(object):
    def maxProfit(self, prices):
        N=len(prices)
        
        result = 0
        
        for i in range(1,N):
            if prices[i-1] < prices[i]:
                result+=prices[i]-prices[i-1]
            else:
                pass
        return result    
    

sol=Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
"""
 
#---------------------------------------------------------------------------

#https://leetcode.com/problems/same-tree/?envType=study-plan-v2&envId=top-interview-150


# Definition for a binary tree node.
""" 
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q :
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right,q.right))
 """    
        
#-----------------------------------------------------------------------------------------------------
#https://leetcode.com/problems/merge-two-sorted-lists/?envType=study-plan-v2&envId=top-interview-150


# Definition for singly-linked list.
""" 
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        temp = ListNode(-1)
        
        current_pos=temp

        while list1 and list2:
            if list1.val < list2.val:
                current_pos.next=list1
                list1=list1.next
            else:
                current_pos.next=list2
                list2=list2.next
            current_pos=current_pos.next
            
        if list1:
            current_pos.next=list1
        elif list2:
            current_pos.next=list2
        
        return temp.next
"""

# 14주차 --------------------------------------------------
#https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

#follow - up 문제 
#만약 S가 수억개 들어오고 t가 1개 있을때 이때도 t를 각각 순회해서 찾을건가? 더 좋은 방법은?!
""" 
class SubsquenceChecker : 
    def __init__(self, t): # t 안에서 각 문자의 위치를 저장해둠
        self.pos = {}
        
        for i, ch in enumerate(t):
            if ch not in self.pos:
                self.pos[ch] = []
                
            self.pos[ch].append(i)
    
    def isSubsequence(self, s):
        prev = -1  # 이전에 찾은 위치
        for ch in s:
            if ch not in self.pos:
                return False  # t에 그 문자가 아예 없음

            found = False
            for idx in self.pos[ch]:
                if idx > prev:  # 이전 위치 뒤에서 찾기
                    prev = idx
                    found = True
                    break
                
            if not found:
                return False
            
        return True

if __name__ == "__main__":
    t = "ahbgdc"          # 기준 문자열
    checker = SubsquenceChecker(t)

    # 테스트 케이스들
    print(checker.isSubsequence("abc"))     # True
    print(checker.isSubsequence("axc"))     # False
    print(checker.isSubsequence(""))        # True
    print(checker.isSubsequence("ahbgdc"))  # True
    print(checker.isSubsequence("aaaa"))    # False

 """





#15주차----------------------------------------------------
""" 
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        
        n=len(gas)
        
        if sum(gas)<sum(cost): #애초부터 못 가면 -1 반환
            return -1
    
        start_pos=0
        tank=0
    
        for i in range(n):
            tank+=gas[i] - cost[i]
            if tank<0:
                start_pos=i+1
                tank=0
                
        return start_pos
<<<<<<< HEAD
            
=======
    
>>>>>>> 32e05abd2a53599f9f70f87d791745713f0e03cc
sol=Solution()
print(sol.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
        
 """


# 16주차 ----------------------------------------------------
#https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150


""" 
class Solution(object):
    def hIndex(self, citations):
        n = len(citations) # n = 5
        count = [0] * (n + 1)

        for c in citations:
            if c >= n: 
                count[n] += 1
            else:
                count[c] += 1

        # 뒤에서부터 누적합 -> 뒤에서 부터 보고 바로 탈출 가능
        
        total = 0
        for i in range(n, -1, -1): #인데스 0번 까지 역방향으로 탈출
            total += count[i]  # i번 이상 인용된 논문 수
            if total >= i:     # 조건 만족 시 h-지수 결정
                return i

        return 0  # 모든 논문 인용이 0인 경우 
        
sol=Solution()
print(sol.hIndex([3,0,6,1,6]))
 """
 
#https://www.acmicpc.net/problem/18111

import sys
input = sys.stdin.readline

N,M,B=map(int,input().split()) #배열 크기 및 가진 블록 개수

ground = [list(map(int,input().split())) for _ in range(N)]

min_height=min(map(min,ground))
max_height=max(map(max,ground))

result_time=float('inf')
result_height=0

for height in range(min_height,max_height+1) : #각 높이마다 탐색 작업 진행
    #height 보다 높으면 블록을 제거 -> 2sec
    #hieght 보다 낮으면 블록을 채움 -> 1sec (단, 인벤토리 블록이 없으면 중단)    
    #이러한 경우 중 가장 적은 최소 시간 탐색 (동일 시간일 경우 가장 높은 높이 출력)
    
    time = 0
    filling_blocks_cnt=B
    for i in range(N):
        for ii in range(M):
            
            diff=ground[i][ii]-height
            
            if diff > 0: #블록이 height 보다 높으면
                time+=diff*2
                filling_blocks_cnt+=diff
            else:
                time+=(-diff)*1
                filling_blocks_cnt-=(-diff)
                
    if filling_blocks_cnt<0:
        continue
        
    if time<result_time or (time==result_time and height > result_height):
        result_time=time
        result_height=height
            
        
            
    
print(result_time,result_height)

