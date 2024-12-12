class Solution:
    def oddString(self, words: List[str]) -> str:
        n=len(words[0])
        difference=[]
        for word in words:
            local_diff=[]
            for i in range(1,len(word)):
                first = ord(word[i-1])-97
                second = ord(word[i])-97
                local_diff.append(second-first)
            difference.append(local_diff)
        occ=defaultdict(int)
        for item in difference:
            occ[tuple(item)]+=1
        result=None
        for key,value in occ.items():
            if value==1:
                result=key
        for i,item in enumerate(difference):
            if item == list(result):
                return words[i]