class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=0
        for ch in sentences:
            count=1
            for i in ch:
                if i==" ":
                    count+=1
            ans=max(ans,count)
        return ans                