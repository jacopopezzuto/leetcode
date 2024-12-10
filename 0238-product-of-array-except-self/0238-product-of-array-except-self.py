class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1,2,3,4]
        1=24 -> 2*3*4
        2=12 -> 1*3*4
        3=8 -> 1*2*4
        4=6 -> 1*2*3
        
        1 1*1 1*1*2 1*1*2*3 1*1*2*3*4
      1*2*3*4*1  2*3*4*1 3*4*1 4*1 1
        
        1 1 2 6 24
        24 24 12 4 1
        
        
        '''
        n=len(nums)
        prefix=[0]*(n+1)
        postfix=[0]*(n+1)
        prefix[0]=1
        postfix[n]=1
        result=[0]*n
        for i in range(1,n+1):
            prefix[i]=prefix[i-1]*nums[i-1]
        for i in range(n-1,-1,-1):
            postfix[i]=postfix[i+1]*nums[i]
        print(prefix)
        print(postfix)
        for i in range(0,n):
            result[i]=prefix[i]*postfix[i+1]
        return result