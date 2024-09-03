class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        acc = [0]*n
        acc[0]=(1 if s[0]=='*' else 0)
        for i in range(1,n):
            acc[i] = acc[i-1]+(1 if s[i]=='*' else 0)

        left_bar_list=[-1]*n
        right_bar_list=[-1]*n
        index_bar=-1
        
        for i in range(n):
            if s[i]=='|':
                index_bar=i
            left_bar_list[i]=index_bar

        index_bar=-1
        for i in range(n-1,-1,-1):
            if s[i]=='|':
                index_bar=i
            right_bar_list[i]=index_bar

        result = []
        for i in range(len(queries)):
            left_bar=left_bar_list[queries[i][1]]
            right_bar=right_bar_list[queries[i][0]]
            query_result=acc[left_bar]-acc[right_bar]
            if query_result<0 or right_bar<0 or left_bar<0:
                result.append(0)   
            else:
                result.append(query_result)

        return result
            
        