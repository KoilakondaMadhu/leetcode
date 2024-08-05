class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dc = 0
        for i in range(len(arr)):
            if self.isd(arr,i):
                dc += 1
                if dc == k:
                    return arr[i]
        return ""
    def isd(self,arr:List[str],index: int)-> bool:
        return arr.count(arr[index]) == 1
