class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dici={}
        ans=True
        n=set()
        for i in arr:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        for j in dici:
            if dici[j] in n:
                ans=False
            else:
                n.add(dici[j])
        return ans
        