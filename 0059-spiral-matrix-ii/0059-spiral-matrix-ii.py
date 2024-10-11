class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        number=1
        #create result matrix
        result= []
        for i in range(0,n):
            result.append([0]*n)
        
        for layer in range(0,(n+1)//2):
            #direction from left to right
            for i in range(layer,n-layer):
                result[layer][i]=number
                number+=1
            #direction from top to bottom
            for i in range(layer+1,n-layer):
                result[i][n-layer-1]=number
                number+=1
            #direction from right to left
            for i in range(n-2-layer,layer-1,-1):
                result[n-1-layer][i]=number
                number+=1
            #direction from bottom to top
            for i in range(n-layer-2,layer,-1):
                result[i][layer]=number
                number+=1
        return result
        
        return None