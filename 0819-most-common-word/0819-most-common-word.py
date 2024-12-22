class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set()
        for item in banned:
            banned_set.add(item)
        words_occurrences=defaultdict(int)
        
        # replace punctuations with spaces
        new_paragraph=[]
        for c in paragraph:
            if c.isalnum():
                new_paragraph.append(c.lower())
            else:
                new_paragraph.append(' ')
        new_paragraph=''.join(new_paragraph)
        print(new_paragraph)
        for word in new_paragraph.split():
            if word not in banned_set:
                words_occurrences[word]+=1
        
        result=""
        max_count=0
        for key,value in words_occurrences.items():
            if value > max_count:
                max_count=value
                result=key
        return result
            