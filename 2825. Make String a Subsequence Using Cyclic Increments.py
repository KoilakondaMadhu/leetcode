class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        targetIdx, targetLen = 0, len(target)
        for currChar in source:
            if targetIdx < targetLEn and (ord(target[targetIdx]) - ord(currChar)) % 26 < 2:
                targetIdx += 1
        return targetIdx == targetLen
