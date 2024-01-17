from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Step 1: Sort the array
        arr.sort()
        v = []  # List to store occurrences

        i = 0
        while i < len(arr):
            cnt = 1  # Initialize count for the current element

            # Count occurrences of the current element
            while i + 1 < len(arr) and arr[i] == arr[i + 1]:
                cnt += 1
                i += 1

            v.append(cnt)  # Append the count to the list
            i += 1  # Move to the next unique element

        v.sort()  # Sort the list of occurrences

        # Step 2: Check for unique occurrences
        for i in range(1, len(v)):
            if v[i] == v[i - 1]:
                return False  # If any adjacent counts are equal, return False

        return True  # If all counts are unique, return True
