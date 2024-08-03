class Solution:
    def canBeEqual(self, targetArray: List[int], currentArray: List[int]) -> bool:
        if len(targetArray) != len(currentArray):
            return False

        elementCounts = [0] * 1001

        for targetNum, currentNum in zip(targetArray, currentArray):
            elementCounts[targetNum] += 1
            elementCounts[currentNum] -= 1

        return all(count == 0 for count in elementCounts)
