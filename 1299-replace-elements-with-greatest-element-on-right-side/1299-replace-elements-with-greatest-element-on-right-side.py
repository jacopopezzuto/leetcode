class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        higher=-1
        count=0
        for i in range(len(arr)-1,-1,-1):
            if higher<arr[i]:
                higher,arr[i]=arr[i],higher
            else:
                arr[i]=higher
        return arr
            