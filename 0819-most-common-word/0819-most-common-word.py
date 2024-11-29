class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        occ={}
        s=set()
        for word in banned:
            s.add(word)
        paragraph=''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])   
        for word in paragraph.split():
            if word in s:
                continue
            if word in occ:
                occ[word]+=1
            else:
                occ[word]=0
        occ=sorted(occ.items(), key=lambda item: item[1], reverse=True)
        return occ[0][0]
        
        