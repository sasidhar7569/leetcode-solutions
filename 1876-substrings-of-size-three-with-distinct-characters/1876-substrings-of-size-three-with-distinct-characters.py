class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l=0
        k=3
        temp=""
        count=0
        for r in range(len(s)):
            temp+=s[r]
            if(r-l==k):
                temp=temp.replace(s[l],"",1)
                l+=1
            if(r-l+1==k):
                if s[l]!=s[l+1] and s[l]!=s[r] and s[l+1]!=s[r]:
                    count+=1
        return count
#         dici={}
# count=0
# for r in range(len(s)):
#   if s[r] not in dici:
#     dici[s[r]]=1
#   else:
#     dici[s[r]]+=1
#   if (r-l==k):
#     dici[s[l]]-=1
#     if dici[s[l]]==0:
#       dici.pop(s[l])
#     l+=1
#   if(r-l+1==k):
#     if len(dici)==k:
#       count+=1
# print(count)