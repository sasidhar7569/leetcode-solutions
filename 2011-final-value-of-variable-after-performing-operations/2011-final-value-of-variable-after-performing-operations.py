class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X=0
        for ch in operations:
            if ch=="X++" or ch=="++X":
                 X+=1
            else:
                X-=1
        return X